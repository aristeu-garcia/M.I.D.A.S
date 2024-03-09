import 'package:flutter/material.dart';
import 'package:midas/constants.dart';
import 'package:midas/pages/dashboard/product%20card.dart';
import 'package:midas/reusableWidgets/fixedCamp.dart';
import 'package:midas/reusableWidgets/systemCard.dart';

class Dashboard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: secondaryColor,
      body: Padding(
        padding: const EdgeInsets.only(
            left: 35, top: 20, right: 40), // Adiciona um padding
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  "Painel de sugestão",
                  style: TextStyle(fontSize: 25, color: mainColor),
                ),
                const SizedBox(
                    height:
                        20), // Adiciona um espaço entre o texto e o FixedCamp
                FixedCamp(
                    text: "Comprar",
                    color: mainColor,
                    icon: Icons.notifications),
                SizedBox(height: 10),
                Row(
                  children: [
                    ProductCard(
                      productName: "CCMU24",
                      textColor: Colors.black,
                      price: "R\$ 129.28",
                      backgroundColor: Colors.white,
                      color: mainColor,
                    ),
                    SizedBox(
                      width: 10,
                    ),
                    ProductCard(
                      productName: "CCMU24",
                      textColor: Colors.black,
                      price: "R\$ 129.90",
                      color: mainColor,
                      backgroundColor: Colors.white,
                    )
                  ],
                ),
                SizedBox(
                  height: 80,
                ),
                FixedCamp(
                    text: "Vender",
                    color: Colors.red[900]!,
                    icon: Icons.warning),
                SizedBox(height: 10),
                Row(
                  children: [
                    ProductCard(
                      productName: "OPF ICF",
                      price: "R\$ 129.28",
                      color: Colors.red[900]!,
                      backgroundColor: Colors.white,
                      textColor: Colors.black,
                    ),
                    SizedBox(
                      width: 10,
                    ),
                    ProductCard(
                      productName: "FUT CCM",
                      price: "R\$ 129.90",
                      textColor: Colors.black,
                      color: Colors.red[900]!,
                      backgroundColor: Colors.white,
                    )
                  ],
                ),
                SizedBox(
                  height: 150,
                ),
                Text(
                  "Ativos Sugeridos",
                  style: TextStyle(fontSize: 25, color: mainColor),
                ),
                SizedBox(
                  height: 10,
                ),
                Row(
                  children: [
                    ProductCard(
                      productName: "Açucar",
                      price: "+36%",
                      backgroundColor: mainColor,
                      textColor: Colors.white,
                      color: Colors.transparent,
                    ),
                    SizedBox(
                      width: 20,
                    ),
                    ProductCard(
                      productName: "Álcool",
                      price: "+6%",
                      textColor: Colors.white,
                      color: Colors.transparent,
                      backgroundColor: mainColor,
                    ),
                    SizedBox(
                      width: 30,
                    ),
                    ProductCard(
                      productName: "Dólar",
                      price: "-9%",
                      textColor: Colors.white,
                      color: Colors.transparent,
                      backgroundColor: Colors.red[900]!,
                    ),
                  ],
                ),
              ],
            ),
            SizedBox(
              width: 30,
            ),
            Column(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                Row(
                  children: [
                    SystemCard('assets/images/image.jpg'),
                    SizedBox(
                      width: 20,
                    ),
                    SystemCard('assets/images/soja.jpg'),
                    SizedBox(
                      width: 20,
                    ),
                    SystemCard('assets/images/senado.jpg'),
                  ],
                ),
                SizedBox(
                  height: 30,
                )
              ],
            )
          ],
        ),
      ),
    );
  }
}
