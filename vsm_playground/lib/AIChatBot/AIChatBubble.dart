import 'package:flutter/material.dart';
import 'package:vsm_playground/AIChatBot/ChatClass.dart';
import 'package:vsm_playground/AIChatBot/SystemChatBubble.dart';

class AIChatBubble extends StatelessWidget {
  MessageClass messageClass;
  AIChatBubble({super.key, required this.messageClass});

  @override
  Widget build(BuildContext context) {
    double margin_value = MediaQuery.of(context).size.width * 0.8 -
        messageClass.message.length * 5;
    return (messageClass.source == 'user')
        ? Container(
            padding: const EdgeInsets.all(20),
            margin: EdgeInsets.only(
                left: (margin_value <= 0 ||
                        margin_value > MediaQuery.of(context).size.width * 0.8)
                    ? MediaQuery.of(context).size.width * 0.3
                    : margin_value,
                right: 10,
                top: 10,
                bottom: 10),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
            ),
            alignment: Alignment.topRight,
            child: Text(messageClass.message),
          )
        : SystemChatBubble(
            margin_value: margin_value, message: messageClass.message);
  }
}
