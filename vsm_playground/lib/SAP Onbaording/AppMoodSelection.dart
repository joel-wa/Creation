// ignore_for_file: no_logic_in_create_state, camel_case_types

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class SAP_OB_appMoodSelection extends StatefulWidget {
  PageController pageController;
  SAP_OB_appMoodSelection({super.key, required this.pageController});

  @override
  State<SAP_OB_appMoodSelection> createState() =>
      _SAP_OB_appMoodSelectionState(pageController);
}

class _SAP_OB_appMoodSelectionState extends State<SAP_OB_appMoodSelection> {
  PageController pageController;
  _SAP_OB_appMoodSelectionState(this.pageController);
  int selected = -1;

  List<String> values = [
    'Classic',
    'Vintage',
    'Energetic',
    'Vibrant',
  ];

  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: MediaQuery.of(context).size.width,
        // height: MediaQuery.of(context).size.height,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            SizedBox(width: MediaQuery.of(context).size.width * 0.25),
            const Text(
              'Choose your theme?',
              style: TextStyle(
                fontSize: 25,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 30),
            SizedBox(
                height:
                    MediaQuery.of(context).size.height * (values.length * 0.1),
                width: MediaQuery.of(context).size.width * 0.8,
                child: ListView.builder(
                    itemCount: values.length,
                    itemBuilder: (BuildContext context, index) {
                      return CheckboxListTile(
                          value: (selected == index) ? true : false,
                          onChanged: (value) {
                            setState(() {
                              selected = (selected != index) ? index : -1;
                            });
                          },
                          title: Text(values[index]));
                    })),
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
