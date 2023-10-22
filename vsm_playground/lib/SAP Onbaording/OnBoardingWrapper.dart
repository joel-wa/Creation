import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../AIChatBot/AIChatPage.dart';
import 'AppMoodSelection.dart';
import 'CategorySelection.dart';
import 'ShopDetailsSelection.dart';

class OnboardingWrapper extends StatefulWidget {
  const OnboardingWrapper({super.key});

  @override
  State<OnboardingWrapper> createState() => _OnboardingWrapperState();
}

class _OnboardingWrapperState extends State<OnboardingWrapper> {
  PageController pageController = PageController();

  @override
  Widget build(BuildContext context) {
    List<int> pv = [];
    List<Widget> wrapperList = [
      AIChatPage(),
      SAP_OB_categorySelect(
        pageController: pageController,
      ),
      SAP_OB_appMoodSelection(
        pageController: pageController,
      ),
      SAP_OB_shopDetails(
        pageController: pageController,
      ),
      AIChatPage(),
    ];
    return Provider(create: (context) {
      pv;
    }, builder: (BuildContext context, child) {
      return Scaffold(
          body: PageView.builder(
              controller: pageController,
              itemCount: wrapperList.length,
              itemBuilder: (BuildContext context, index) {
                return wrapperList[index];
              }));
    });
  }
}
