import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:vsm_playground/AIChatBot/ChatClass.dart';

class SystemChatBubble extends StatelessWidget {
  double margin_value;
  String message;

  SystemChatBubble(
      {super.key, required this.margin_value, required this.message});

  List<String> commandList = [];
  int command_count = 0;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      margin: EdgeInsets.only(
          right: (margin_value <= 0 ||
                  margin_value > MediaQuery.of(context).size.width * 0.8)
              ? MediaQuery.of(context).size.width * 0.4
              : margin_value,
          left: 10,
          top: 10,
          bottom: 10),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(10),
      ),
      alignment: Alignment.topRight,
      child: Column(children: [
        Text(parseMessage()),
        ListView.builder(
            shrinkWrap: true,
            itemCount: commandList.length,
            itemBuilder: (BuildContext context, index) {
              return Padding(
                padding: const EdgeInsets.all(8.0),
                child: customButton(context, commandList[index]),
              );
            })
      ]),
    );
  }

  String parseMessage() {
    String value = message;
    String _message = """""";
    String _command = '';
    bool flag = false;
    for (var i = 0; i < value.length; i++) {
      if (value[i] == '<') {
        flag = true;
        command_count += 1;
        // continue;
      }
      if (flag) {
        _command += value[i];
        // continue;
      }
      if (i >= 1) {
        if (value[i - 1] == '>') {
          print(_command);
          commandList.add(_command);
          _command = '';
          print(commandList);
          flag = false;
          // continue;
        }
      }
      if (!flag) {
        _message += value[i];
      }
    }
    return _message;
  }

  Widget customButton(BuildContext context, String _command) {
    final value = _command.trim();
    return ElevatedButton.icon(
        icon: Icon(Icons.lightbulb_outline),
        onPressed: () {
          // Navigator.of(context)
          //     .push(MaterialPageRoute(builder: (BuildContext context) {
          //   return;
          // }));
          ChatClass.chat.add(MessageClass('user', value));
        },
        label: Text(
          value.toString(),
        ));
  }
}
