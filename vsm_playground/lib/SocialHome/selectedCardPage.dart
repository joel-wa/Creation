import 'package:flutter/material.dart';

class SelectedCardPage extends StatelessWidget {
  final String information;

  const SelectedCardPage({Key? key, required this.information})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Title")),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Hero(
            tag: information,
            child: ClipRRect(
              borderRadius: BorderRadius.circular(10),
              child: Material(
                // color: Colors.transparent,
                child: InkWell(
                  onTap: () {
                    Navigator.of(context).pop();
                  },
                  child: Container(
                    height: 400, // Adjust as needed
                    color: Colors.white,
                    child: Center(child: Text(information)),
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
