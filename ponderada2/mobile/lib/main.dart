import 'dart:ffi';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'dart:convert';

void main() async {
  await dotenv.load(fileName: "lib/.env");
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: "Pablinho's App"),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController _controllername = TextEditingController();
  final TextEditingController _controllerdata = TextEditingController();
  final TextEditingController _controllerpostedit = TextEditingController();
  final TextEditingController _controllercontentedit = TextEditingController();
  List all_notes = [];

  void initState() {
    super.initState();
    print("INIT STATE CALLED");
    getAllPosts();
    print("got all posts.");
  }

  void requestCaller() async {
    var resposta = await http.post(Uri.parse("http://${dotenv.env['IP']}:5000/users"),
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode({
          'username': _controllername.text,
          'password': _controllerdata.text
        }));
    setState(() {
      getAllPosts();
      print("got all posts.");
    });

    print(resposta.body);
  }

  void postEditor(id) async {
    var resposta = await http.put(
        Uri.parse("http://${dotenv.env['IP']}:5000/users/${id}"),
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode({
          'username': _controllerpostedit.text,
          'password': _controllercontentedit.text
        }));
    setState(() {
      getAllPosts();
      print("got all posts.");
    });

    print(resposta.body);
  }

  void postDeleter(id) async {
    var resposta = await http.delete(
      Uri.parse("http://${dotenv.env['IP']}:5000/users/${id}"),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
    );
    setState(() {
      getAllPosts();
      print("got all posts.");
    });

    print(resposta.body);
  }

  void getAllPosts() async {
    var resposta = await http.get(Uri.parse("http://${dotenv.env['IP']}:5000/users"));

    var processedanswer = jsonDecode(resposta.body);
    print(resposta.body);
    setState(() {
      all_notes = [];
      all_notes = processedanswer;
    });

    print(all_notes.length);
  }

  void showMyDialog() async {
    return showDialog<void>(
      context: context,
      builder: (BuildContext context) => AlertDialog(
        title: const Text('Adicionar Anotação'),
        content: const Text('Preencha os campos adequadamente'),
        actions: <Widget>[
          TextField(
            controller: _controllername,
            decoration: const InputDecoration(
                border: OutlineInputBorder(), labelText: 'Username'),
          ),
          TextField(
            controller: _controllerdata,
            decoration: const InputDecoration(
                border: OutlineInputBorder(), labelText: 'Password'),
          ),
          Row(
            children: [
              TextButton(
                onPressed: () => Navigator.pop(context, 'Cancelar'),
                // onPressed: () => getAllPosts(),

                child: const Text('Cancelar'),
              ),
              TextButton(
                onPressed: () {
                  requestCaller();
                  Navigator.pop(context, 'Adicionar');
                },
                child: const Text('Adicionar'),
              ),
            ],
          )
        ],
      ),
    );
  }

  void showDialogPosts(postid, username, password) async {
    _controllerpostedit.text = username;
    _controllercontentedit.text = password;
    return showDialog<void>(
      context: context,
      builder: (BuildContext contexteditor) => AlertDialog(
        title: const Text('Editar Anotação'),
        content: const Text('Atualize os campos conforme desejado'),
        actions: <Widget>[
          TextField(
            controller: _controllerpostedit,
            decoration: const InputDecoration(
                border: OutlineInputBorder(), labelText: 'Username'),
          ),
          TextField(
            controller: _controllercontentedit,
            decoration: const InputDecoration(
                border: OutlineInputBorder(), labelText: 'Password'),
          ),
          Row(
            children: [
              TextButton(
                onPressed: () => Navigator.pop(contexteditor, 'Cancelar'),
                // onPressed: () => getAllPosts(),

                child: const Text('Cancelar'),
              ),
              TextButton(
                onPressed: () {
                  postEditor(postid);
                  Navigator.pop(contexteditor, 'Atualizar');
                },
                child: const Text('OK'),
              ),
            ],
          )
        ],
      ),
    );
  }

  void showDialogPostsDelete(postid) async {
    return showDialog<void>(
      context: context,
      builder: (BuildContext contextdeleter) => AlertDialog(
        title: const Text('Você tem certeza?'),
        content: const Text('Deletar tarefa do Note Book?'),
        actions: <Widget>[
          Row(
            children: [
              TextButton(
                onPressed: () => Navigator.pop(contextdeleter, 'Cancelar'),
                // onPressed: () => getAllPosts(),

                child: const Text('Cancelar'),
              ),
              TextButton(
                onPressed: () {
                  postDeleter(postid);
                  Navigator.pop(contextdeleter, 'Deletar');
                },
                child: const Text('OK'),
              ),
            ],
          )
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.primary,
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          verticalDirection: VerticalDirection.down,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const Text("Note Book",
                style: TextStyle(
                    fontWeight: FontWeight.bold, fontSize: 26, height: 2)),
            ListView.builder(
                itemCount: all_notes.length,
                scrollDirection: Axis.vertical,
                shrinkWrap: true,
                itemBuilder: (context, index) {
                  return ListTile(
                      // title:Text("${all_notes[index]}")
                      title: Container(
                    decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(8.0),
                        border:
                            const Border.fromBorderSide(BorderSide(width: 2))),
                    alignment: Alignment.center,
                    width: 300,
                    height: 130,
                    child: Column(
                      children: [
                        Text("Username: ${all_notes[index]["username"]}"),
                        Text("Password: ${all_notes[index]["password"]}"),
                        Align(
                            alignment: Alignment.bottomRight,
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                TextButton(
                                    onPressed: () {
                                      showDialogPosts(
                                          all_notes[index]['id'],
                                          all_notes[index]['username'],
                                          all_notes[index]["password"]);
                                    },
                                    child: const Icon(
                                      Icons.edit,
                                      size: 20,
                                      color: Colors.yellow,
                                    )),
                                TextButton(
                                    onPressed: () {
                                      showDialogPostsDelete(
                                          all_notes[index]['id']);
                                    },
                                    child: const Icon(
                                      Icons.delete,
                                      size: 20,
                                      color: Colors.red,
                                    )),
                              ],
                            )),
                      ],
                    ),
                  ));
                }),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          showMyDialog();
        },
        child: const Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
