import 'package:flutter/material.dart';
import 'package:flutter_staggered_grid_view/flutter_staggered_grid_view.dart';
import 'package:vsm_playground/SocialHome/selectedCardPage.dart';

class SocialHomePage extends StatefulWidget {
  const SocialHomePage({Key? key}) : super(key: key);

  @override
  State<SocialHomePage> createState() => _SocialHomePageState();
}

class _SocialHomePageState extends State<SocialHomePage> {
  int _currentIndex = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: MasonryGridView.builder(
          gridDelegate: const SliverSimpleGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2,
          ),
          mainAxisSpacing: 10,
          crossAxisSpacing: 8,
          itemBuilder: (BuildContext context, index) {
            return GestureDetector(
              onTap: () {
                Navigator.of(context).push(
                  MaterialPageRoute(
                    builder: (BuildContext context) {
                      return SelectedCardPage(
                        information: "Card number $index",
                      );
                    },
                  ),
                );
              },
              child: Container(
                height: (index % 2 == 0) ? 250 + 30 : 200 + 30,
                child: Column(
                  children: [
                    Hero(
                      tag: "Card number $index",
                      child: ClipRRect(
                        borderRadius: BorderRadius.circular(10),
                        child: Container(
                          height: (index % 2 == 0) ? 250 : 200,
                          color: Colors.red,
                          child: Stack(
                              alignment: Alignment.bottomCenter,
                              children: [
                                Center(
                                  child: Text("$index"),
                                ),
                                const Positioned(
                                  bottom: 5,
                                  child: CircleAvatar(
                                    radius: 25,
                                  ),
                                ),
                              ]),
                        ),
                      ),
                    ),
                    Text("Shop Name", style: TextStyle(color: Colors.white)),
                    const SizedBox(height: 5),
                  ],
                ),
              ),
            );
          },
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        // useLegacyColorScheme: false,
        backgroundColor: Colors.black,
        currentIndex: _currentIndex,
        selectedItemColor: Colors.black,
        unselectedItemColor: Colors.grey,
        onTap: (int index) {
          setState(() {
            _currentIndex = index;
          });
          // Handle navigation based on the selected index
          // You can implement different actions for each tab here
        },
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.search),
            label: 'Explore',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.add),
            label: 'Add',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.favorite),
            label: 'Favorites',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: 'Profile',
          ),
        ],
      ),
    );
  }
}
