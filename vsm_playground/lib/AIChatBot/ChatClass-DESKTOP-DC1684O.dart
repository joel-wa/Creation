import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class ChatClass {
  final url = 'http://localhost:5000/';
  //  'http://ec2-3-135-228-10.us-east-2.compute.amazonaws.com:5000/';
  static List<MessageClass> chat = [
    MessageClass('system', """Welcome to VSM Mobile Assistant!

I'm here to help you manage your mobile app. Tell me what you need, and I'll provide the help to get it done. How can I assist you today?"""),
    MessageClass('system',
        """Try using one of the links to navigate the app<nav:Dashboard> <nav:Orders> """),
  ];
  static bool canSend = true;
  String answer = '';

  Future<void> userSendMessage(
      String message, ScrollController controller) async {
    chat.add(MessageClass('user', message));
    if (canSend == false) {
      chat.add(MessageClass('system', 'please wait'));
      return;
    }
    canSend = false;
    await createPost(message);
    controller.position.animateTo(controller.position.maxScrollExtent,
        duration: const Duration(milliseconds: 500), curve: Curves.linear);
    canSend = true;
    return;
  }

  Future<String> fetchPost() async {
    try {
      final response = await http.get(Uri.parse('${url}aiChat'));
      print(response);
      // return 'hello';
      if (response.statusCode == 201) {
        // Successful response
        // print('Response data: ${response.body}');
        answer = response.body;
        return answer;
      } else {
        // Handle the error
        print('Request failed with status: ${response.statusCode}');
        return 'Error';
      }
    } catch (e) {
      print(' Fetch Error: $e');
      return 'Error';
    }
  }

  Future<bool> createPost(String body) async {
//     chat.add(MessageClass('system', """
// Hi you can go to the Dashboard by tapping the link below:
//   <nav:Dashboard>
//   <nav:AddProductPage>
// // Feel free to ask any other questions
// """));
//     return true;
    final response = await http.post(
      Uri.parse('${url}aiChat'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(body),
    );

    if (response.statusCode == 201) {
      final parsedData = response.body;
      chat.add(MessageClass('system', parsedData));

      return true;
    } else {
      print('Request failed with status: ${response.statusCode}');
      return false;
    }
  }
}

Future<bool> createPost(String body) async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/ai_chat'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(body),
  );

  if (response.statusCode == 201) {
    final parsedData = json.decode(response.body);
    print('Post created with ID: ${parsedData['id']}');
    return true;
  } else {
    print('Request failed with status: ${response.statusCode}');
    return false;
  }
}

class MessageClass {
  String source;
  String message;
  MessageClass(this.source, this.message);
}
