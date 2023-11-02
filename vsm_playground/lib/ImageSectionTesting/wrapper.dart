import 'package:flutter/material.dart';
import 'package:vsm_playground/ImageSectionTesting/Addimage.dart';

class ImageWrapper extends StatefulWidget {
  const ImageWrapper({super.key});

  @override
  State<ImageWrapper> createState() => _ImageWrapperState();
}

class _ImageWrapperState extends State<ImageWrapper> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text('Image Wrapper')),
        backgroundColor: Color.fromARGB(255, 36, 3, 36),
        body: SingleChildScrollView(
            child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.all(20),
              child: AddImageBox(),
            )
          ],
        )));
  }
}
