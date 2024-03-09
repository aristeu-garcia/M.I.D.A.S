import 'package:flutter/material.dart';

class VeryLargeInsertCamp extends StatelessWidget {
  final TextEditingController controller;

  const VeryLargeInsertCamp({Key? key, required this.controller})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Positioned(
      top: 0, // Define a posição superior
      left: 0, // Define a posição esquerda
      child: LayoutBuilder(
        builder: (BuildContext context, BoxConstraints constraints) {
        
          return Container(
            width: double.infinity, // Largura adaptativa
            height: 40,
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(180.0),
              boxShadow: [
                BoxShadow(
                  color: Colors.grey.withOpacity(0.5),
                  spreadRadius: 2,
                  blurRadius: 7,
                  offset: Offset(0, 3),
                ),
              ],
            ),
            child: Center(
              child: TextField(
                controller: controller,
                textAlignVertical: TextAlignVertical.center,
                textAlign: TextAlign.start,
                decoration: InputDecoration(
                  border: InputBorder.none,
                  hintText: '',
                ),
                keyboardType: TextInputType.multiline,
                style: TextStyle(fontSize: 18, color: Colors.grey[900]),
              ),
            ),
          );
        },
      ),
    );
  }
}
