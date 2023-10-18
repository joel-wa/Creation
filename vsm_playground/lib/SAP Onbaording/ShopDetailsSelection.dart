import 'package:flutter/material.dart';

class SAP_OB_shopDetails extends StatefulWidget {
  PageController pageController;
  SAP_OB_shopDetails({super.key, required this.pageController});

  @override
  State<SAP_OB_shopDetails> createState() =>
      _SAP_OB_shopDetailsState(pageController);
}

class _SAP_OB_shopDetailsState extends State<SAP_OB_shopDetails> {
  PageController pageController;
  _SAP_OB_shopDetailsState(this.pageController);
  @override
  Widget build(BuildContext context) {
    return Container(
        width: MediaQuery.of(context).size.width * 0.9,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              height: 150,
              width: MediaQuery.of(context).size.width * 0.8,
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
            const SizedBox(height: 50),
            Container(
                // margin: const EdgeInsets.all(20),
                // height: 400,
                width: MediaQuery.of(context).size.width * 0.8,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const CircleAvatar(
                      radius: 50,
                      child: Icon(
                        Icons.camera_alt,
                        size: 30,
                      ),
                    ),
                    const SizedBox(width: 30),
                    Container(
                      height: 50,
                      width: MediaQuery.of(context).size.width * 0.5,
                      padding: const EdgeInsets.all(15),
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(20),
                        color: const Color.fromARGB(255, 212, 212, 212),
                      ),
                      child: const TextField(
                        decoration: InputDecoration(
                          border: InputBorder.none,
                        ),
                      ),
                    )
                  ],
                )),
            const SizedBox(height: 50),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                ElevatedButton(
                    onPressed: () {
                      pageController.previousPage(
                          duration: const Duration(milliseconds: 500),
                          curve: Curves.linear);
                    },
                    child: const Text('Back')),
                ElevatedButton(
                    onPressed: () {
                      pageController.nextPage(
                          duration: const Duration(milliseconds: 500),
                          curve: Curves.linear);
                    },
                    child: const Text('Continue')),
              ],
            ),
          ],
        ));
  }
}
