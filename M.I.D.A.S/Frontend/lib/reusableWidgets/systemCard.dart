import 'package:flutter/material.dart';

class SystemCard extends StatelessWidget {
  final String imageName;

  SystemCard(
    this.imageName, {
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 170, // Ajuste a largura conforme necessário
      height: 280, // Ajuste a altura conforme necessário
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(
            20), // Define a borda arredondada do container
        color: Colors.white, // Define a cor de fundo como branco
        boxShadow: [
          BoxShadow(
            color: Colors.grey.withOpacity(1),
            blurRadius: 20,
          ),
        ],
      ),
      padding: const EdgeInsets.all(8), // Adiciona um padding interno
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Expanded(
            child: Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(180),
              ),
              child: GestureDetector(
                onTap: () async {
                  // Adicione aqui a ação que deseja realizar ao tocar no card
                },
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(16),
                  child: Stack(
                    children: [
                      Image.asset(
                        imageName, // Usando o caminho recebido via construtor
                        height: 170, // Ajuste a altura conforme necessário
                        width: 170, // Ajuste a largura conforme necessário
                        fit: BoxFit.cover,
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
          SizedBox(
              height:
                  5), // Adiciona um espaço entre a imagem e o texto de descrição
          Text(
            "Contrado novembro da soja rompe expectativas",
            style: TextStyle(
              fontSize: 14,
              color: Colors.black,
            ),
          ),
          SizedBox(height: 20),
          Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              Text(
                "O estadão",
                style: TextStyle(
                  fontSize: 14,
                  color: Colors.black,
                ),
              ),
            ],
          ), // Adiciona um espaço entre a imagem e o texto de descrição
        ],
      ),
    );
  }
}
