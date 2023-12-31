import 'dart:convert';

import 'package:flutter/material.dart';

class CodeView extends StatefulWidget {
  const CodeView({Key? key}) : super(key: key);

  @override
  State<CodeView> createState() => _CodeViewState();
}

class _CodeViewState extends State<CodeView> {
  Map<String, dynamic> code = {
    "height": 120,
    "width": 250,
    "borderRadius": 8,
    "backgroundColor": "#87CEEB",
  };

  @override
  Widget build(BuildContext context) {
    print(code);
    return Scaffold(
      body: Center(
        child: Container(
          height: code['height'],
          width: code['width'],
          decoration: BoxDecoration(
            color: Colors.red,
            borderRadius: BorderRadius.circular(code['borderRadius']),
          ),
          child: Center(child: Text(code.toString())),
        ),
      ),
    );
  }
}
