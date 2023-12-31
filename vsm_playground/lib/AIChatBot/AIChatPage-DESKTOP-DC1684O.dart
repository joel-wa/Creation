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
  ScrollController controller = ScrollController();
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
              color: Color.fromARGB(255, 210, 170, 215),
              padding: const EdgeInsets.only(bottom: 10),
              child: ChatRenderer(
                controller: controller,
              ),
            ),
            Positioned(
              bottom: 0,
              child: Container(
                color: const Color.fromARGB(255, 255, 255, 255),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: [
                    Container(
                      height: 40,
                      width: 40,
                      margin: const EdgeInsets.all(15),
                      decoration: BoxDecoration(
                        color: const Color.fromARGB(255, 212, 212, 212),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: const Center(
                        child: Icon(
                          Icons.camera_alt,
                          size: 30,
                        ),
                      ),
                    ),
                    //TextField
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Container(
                        height: textFieldHeight,
                        width: MediaQuery.of(context).size.width * 0.65,
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
                    // const SizedBox(width: 5),

                    //
                    Container(
                      height: 70,
                      width: 70,
                      child: IconButton(
                          onPressed: () async {
                            if (textEditingController.value.text == '') return;
                            await ChatClass().userSendMessage(
                                textEditingController.value.text, controller);
                            textEditingController.clear();

                            setState(() {});
                          },
                          icon: const Icon(Icons.send, size: 30)),
                    )
                  ],
                ),
              ),
            )
          ],
        ));
  }
}
