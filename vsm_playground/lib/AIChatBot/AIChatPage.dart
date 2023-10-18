import 'package:flutter/material.dart';
import 'package:vsm_playground/AIChatBot/AIChatRenderer.dart';
import 'package:vsm_playground/AIChatBot/ChatClass.dart';

class AIChatPage extends StatefulWidget {
  const AIChatPage({super.key});

  @override
  State<AIChatPage> createState() => _AIChatPageState();
}

class _AIChatPageState extends State<AIChatPage> {
  TextEditingController textEditingController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    String targetChar = "\n";
    double result =
        textEditingController.value.text.split(targetChar).length - 1;

    double other_r = textEditingController.value.text.length /
        MediaQuery.of(context).size.width *
        10;
    double textFieldHeight = 55 + (18 * (result + other_r.ceil()));
    return Container(
        height: MediaQuery.of(context).size.height * 0.99,
        child: Stack(
          alignment: Alignment.topCenter,
          // mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: [
            Container(
              height: MediaQuery.of(context).size.height * 0.89,
              color: Colors.yellow,
              child: ChatRenderer(),
            ),
            Positioned(
              bottom: 0,
              child: Container(
                color: Colors.white,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: [
                    //TextField
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Container(
                        height: textFieldHeight,
                        width: MediaQuery.of(context).size.width * 0.8,
                        // padding: const EdgeInsets.all(10),
                        decoration: BoxDecoration(
                          border: Border.all(width: 0.5, color: Colors.grey),
                          borderRadius: BorderRadius.circular(20),
                          color: const Color.fromARGB(255, 212, 212, 212),
                        ),
                        child: Padding(
                          padding: const EdgeInsets.all(5.0),
                          child: TextField(
                            controller: textEditingController,
                            maxLines: 10,
                            onChanged: (value) {
                              setState(() {
                                textFieldHeight;
                              });
                            },
                            decoration: const InputDecoration(
                              border: InputBorder.none,
                            ),
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 10),

                    //
                    Container(
                      height: 70,
                      width: 70,
                      child: IconButton(
                          onPressed: () {
                            if (textEditingController.value.text == '') return;
                            setState(() {
                              ChatClass().userSendMessage(
                                  textEditingController.value.text);
                              textEditingController.clear();
                            });
                          },
                          icon: const Icon(Icons.send)),
                    )
                  ],
                ),
              ),
            )
          ],
        ));
  }
}
