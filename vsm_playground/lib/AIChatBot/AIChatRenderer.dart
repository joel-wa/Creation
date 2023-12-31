import 'package:flutter/material.dart';
// import 'package:vsm_playground/AIChatBot/AIChatBubble.dart';
import 'package:vsm_playground/AIChatBot/ChatClass.dart';

import 'AIChatBubble-DESKTOP-DC1684O.dart';

class ChatRenderer extends StatefulWidget {
  ScrollController controller;
  ChatRenderer({super.key, required this.controller});

  @override
  State<ChatRenderer> createState() => _ChatRendererState(controller);
}

class _ChatRendererState extends State<ChatRenderer> {
  ScrollController controller;
  _ChatRendererState(this.controller);
  @override
  Widget build(BuildContext context) {
    // return f_b(controller);
    return ListView.builder(
      controller: controller,
      itemCount: ChatClass.chat.length,
      itemBuilder: (BuildContext context, index) {
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
