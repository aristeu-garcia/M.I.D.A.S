import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'pages/login/login.dart';

void main() {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    SystemChrome.setPreferredOrientations([
      DeviceOrientation.portraitDown,
      DeviceOrientation.portraitUp,
    ]);
    SystemChrome.setSystemUIOverlayStyle(
      const SystemUiOverlayStyle(
        statusBarColor: Colors.transparent,
        statusBarBrightness: Brightness.light,
      ),
    );

    return  MaterialApp(
        title: 'M.I.D.A.S',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          primaryColor: Colors.green, 
          fontFamily: "Quicksand",
        ),
        home: LoginScreen(),
      
    );
  }
}