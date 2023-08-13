import 'package:flutter/material.dart';
import 'package:untitled_icons/untitled_icons.dart';

void main() => runApp(const MyApp());

const _untitledPrimaryColor = Color(0xFF6941C6);

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Untitled Icons Example',
      theme: ThemeData(
        useMaterial3: true,
        primaryColor: _untitledPrimaryColor,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Untitled Icons Example'),
          centerTitle: true,
        ),
        body: const Center(
          child: UntitledIcon(
            icon: UntitledGeneral.checkVerified02,
            size: 150,
          ),
        ),
      ),
    );
  }
}
