import 'package:flutter/material.dart';
import 'package:vsm_playground/AIChatBot/AIChatBubble.dart';
import 'package:vsm_playground/AIChatBot/ChatClass.dart';

class ChatRenderer extends StatefulWidget {
  const ChatRenderer({super.key});

  @override
  State<ChatRenderer> createState() => _ChatRendererState();
}

class _ChatRendererState extends State<ChatRenderer> {
  ScrollController controller = ScrollController();
  @override
  Widget build(BuildContext context) {
    // return f_b(controller);
    return ListView.builder(
      controller: controller,
      itemCount: ChatClass.chat.length,
      itemBuilder: (BuildContext context, index) {
        controller.position.animateTo(controller.position.maxScrollExtent,
            duration: const Duration(milliseconds: 500), curve: Curves.linear);
        return AIChatBubble(messageClass: ChatClass.chat[index]);
      },
    );
  }
}

Widget f_b(ScrollController controller) {
  return FutureBuilder(
      future: ChatClass().createPost('Going'),
      builder: (BuildContext context, snapshot) {
        return Text(snapshot.data as String);
      });
}
