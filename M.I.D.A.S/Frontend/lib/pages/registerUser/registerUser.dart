import 'package:flutter/material.dart';
import '../../reusableWidgets/insertCamp.dart';
import '../../reusableWidgets/halfInsertCampPassword.dart';
import '../../reusableWidgets/halfInsertCamp.dart';
import '../../reusableWidgets/roundedButtom.dart';
import 'package:midas/constants.dart';

class RegisterUser extends StatelessWidget {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Removendo a barra azul
      body: Container(
        // Definindo a cor de fundo
        color: mainColor,
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 40.0), // Ajuste aqui
          child: Column(
            children: [
              Row(
                children: [
                  SizedBox(width: 20),
                  Column(
                    children: [
                      ElevatedButton(
                        onPressed: () => Navigator.of(context).pop(),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.white,
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(180.0),
                          ),
                          minimumSize: Size(150, 50),
                        ),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(Icons.arrow_back_ios,
                                color: mainColor, size: 20),
                            SizedBox(width: 3),
                            Text(
                              "Voltar",
                              style:
                                  TextStyle(color: mainColor, fontSize: 20),
                            ),
                          ],
                        ),
                      )
                    ],
                  )
                ],
              ),
              Expanded(
                child: SingleChildScrollView(
                  physics: AlwaysScrollableScrollPhysics(),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      SizedBox(height: 20),
                      Center(
                        child: Container(
                          height: 240,
                          width: 240,
                          child: Padding(
                            padding: EdgeInsets.all(4),
                            child: Container(
                              color: Colors.transparent,
                              child: Image.asset(
                                'assets/images/logoMidas.png',
                              ),
                            ),
                          ),
                        ),
                      ),
                      SizedBox(height: 20),
                      Center(
                        child: SizedBox(
                          width: 450,
                          height: 395,
                          child: Card(
                            color: mainColor,
                            elevation: 5,
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(100),
                              side: BorderSide(
                                color: Colors.white,
                                width: 10,
                              ),
                            ),
                            child: Container(
                              padding: EdgeInsets.all(20),
                              child: Column(
                                children: [
                                  Row(
                                    mainAxisAlignment: MainAxisAlignment.center,
                                    children: [
                                      Text(
                                        'Criar Conta',
                                        style: TextStyle(
                                          fontSize: 22,
                                          color: Colors.white,
                                        ),
                                      ),
                                    ],
                                  ),
                                  SizedBox(height: 10),
                                  Column(
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    children: [
                                      Text(
                                        'Nome completo',
                                        style: TextStyle(
                                          fontSize: 20,
                                          color: Colors.white,
                                        ),
                                      ),
                                      SizedBox(height: 3),
                                      RoundedTextField(
                                          controller: emailController),
                                    ],
                                  ),
                                  SizedBox(height: 5),
                                  Column(
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    children: [
                                      Text(
                                        'Email',
                                        style: TextStyle(
                                          fontSize: 20,
                                          color: Colors.white,
                                        ),
                                      ),
                                      SizedBox(height: 3),
                                      RoundedTextField(
                                          controller: emailController),
                                    ],
                                  ),
                                  SizedBox(height: 5),
                                  Column(
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    children: [
                                      Text(
                                        'Telefone',
                                        style: TextStyle(
                                          fontSize: 20,
                                          color: Colors.white,
                                        ),
                                      ),
                                      SizedBox(height: 3),
                                      HalfroundedTextField(
                                          controller: passwordController),
                                      SizedBox(height: 5),
                                      Text(
                                        'Senha',
                                        style: TextStyle(
                                          fontSize: 20,
                                          color: Colors.white,
                                        ),
                                      ),
                                      SizedBox(height: 3),
                                      HalfroundedTextFieldPassword(
                                          controller: passwordController),
                                      SizedBox(height: 5),
                                      Text(
                                        'Confirmar senha',
                                        style: TextStyle(
                                          fontSize: 20,
                                          color: Colors.white,
                                        ),
                                      ),
                                      SizedBox(height: 3),
                                      HalfroundedTextFieldPassword(
                                          controller: passwordController),
                                      SizedBox(height: 15),
                                      Center(
                                        child: RoundedButton(
                                          onPressed: () => {},
                                          text: "Cadastrar",
                                        ),
                                      ),
                                    ],
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ),
                      ),
                      SizedBox(
                        width: 1,
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}