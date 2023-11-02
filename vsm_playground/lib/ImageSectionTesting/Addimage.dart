import 'package:flutter/material.dart';

class AddImageBox extends StatefulWidget {
  const AddImageBox({super.key});

  @override
  State<AddImageBox> createState() => _AddImageBoxState();
}

class _AddImageBoxState extends State<AddImageBox> {
  List images = [1, 2, 3, 4];
  @override
  Widget build(BuildContext context) {
    return Container(
        height: 200,
        child: ListView.builder(
            itemCount: images.length + 1,
            scrollDirection: Axis.horizontal,
            itemBuilder: (BuildContext context, index) {
              return (index == 0)
                  ? GestureDetector(
                      onTap: () {
                        setState(() {
                          images.add(1);
                        });
                      },
                      child: Container(
                        margin: const EdgeInsets.all(5),
                        // height: 200,
                        width: 200,
                        color: Color.fromARGB(255, 52, 4, 52),
                      ),
                    )
                  : GestureDetector(
                      onTap: () {
                        setState(() {
                          images.removeLast();
                        });
                      },
                      child: Container(
                        margin: const EdgeInsets.all(5),
                        height: 200,
                        width: 200,
                        color: Color.fromARGB(255, 190, 39, 190),
                      ),
                    );
            }));
  }
}
