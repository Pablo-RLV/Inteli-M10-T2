import 'package:flutter/material.dart';
import '../controllers/auth_controller.dart';
import '../models/user.dart';

class LoginPage extends StatelessWidget {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  LoginPage({super.key});

  Future<void> _login(BuildContext context) async {
    final email = _emailController.text;
    final password = _passwordController.text;
    final user = User(email: email, password: password);
    await AuthController.login(user, context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.indigo[300],
      appBar: AppBar(
        title: const Text(
          'Sign in',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: Colors.indigo[900],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            TextField(
              controller: _emailController,
              decoration: const InputDecoration(labelText: 'User', labelStyle: TextStyle(color: Colors.indigo)),
            ),
            TextField(
              controller: _passwordController,
              decoration: const InputDecoration(labelText: 'Password', labelStyle: TextStyle(color: Colors.indigo)),
              obscureText: true,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.indigo,
                    foregroundColor: Colors.white
                  ),
              onPressed: () => _login(context),
              child: const Text('Sign in'),
            ),
            TextButton(
              style: TextButton.styleFrom(
                    foregroundColor: Colors.white
                  ),
              onPressed: () {
                Navigator.pushNamed(context, '/signup');
              },
              child: const Text('Sign up'),
            ),
          ],
        ),
      ),
    );
  }
}
