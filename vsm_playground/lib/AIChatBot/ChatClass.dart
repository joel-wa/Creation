import 'dart:convert';

import 'package:http/http.dart' as http;

class ChatClass {
  static List<MessageClass> chat = [];

  Future<void> userSendMessage(String message) async {
    chat.add(MessageClass('user', message));
    bool result = await createPost(message);
    if (result) {
      String answer = await fetchPost();
      chat.add(MessageClass('system', answer));
    } else {
      chat.add(MessageClass('system', 'error'));
    }
  }

  Future<String> fetchPost() async {
    try {
      final response = await http.get(Uri.parse('http://localhost:5000/'));

      if (response.statusCode == 200) {
        // Successful response
        print('Response data: ${response.body}');
        return response.body;
      } else {
        // Handle the error
        print('Request failed with status: ${response.statusCode}');
        return 'Error';
      }
    } catch (e) {
      print('Error: $e');
      return 'Error';
    }
  }

  Future<bool> createPost(String body) async {
    try {
      final response = await http.post(
        Uri.parse('http://localhost:5000/ai'),
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode(body), // Wrap body in an object
      );

      if (response.statusCode == 201) {
        final parsedData = json.decode(response.body);
        print('Post created with ID: ${parsedData['id']}');
        return true;
      } else {
        print('Post Request failed with status: ${response.statusCode}');
        return false;
      }
    } catch (e) {
      print('Create Post Error: $e');
      return false;
    }
  }
}

Future<bool> createPost(String body) async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/ai'),
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
