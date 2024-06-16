import 'dart:io';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import '../controllers/image_controller.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  MyHomePageState createState() => MyHomePageState();
}

class MyHomePageState extends State<MyHomePage> {
  File? _image;
  Uint8List? _processedImage;
  final ImagePicker _picker = ImagePicker();

  Future<void> _pickImageFromCamera() async {
  final pickedFile = await _picker.pickImage(source: ImageSource.camera);

  setState(() {
    if (pickedFile != null) {
      _image = File(pickedFile.path);
      _processedImage = null;
    } else {
      print('Nenhuma imagem capturada.');
    }
  });
}

  Future<void> _pickImage() async {
    final pickedFile = await _picker.pickImage(source: ImageSource.gallery);

    setState(() {
      if (pickedFile != null) {
        _image = File(pickedFile.path);
        _processedImage = null;
      } else {
        print('Nenhuma imagem selecionada.');
      }
    });
  }

  Future<void> _sendImage() async {
    if (_image == null) return;

    _showLoadingDialog();
    final processedImage = await ImageController.sendImage(_image!);
    Navigator.of(context).pop();

    setState(() {
      _processedImage = processedImage;
      _image = null;
    });

    if (_processedImage != null) {
      _showProcessedImageDialog();
    } else {
      print('Falha ao processar a imagem.');
    }
  }

  void _showLoadingDialog() {
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return const AlertDialog(
          backgroundColor: Colors.transparent,
          elevation: 0,
          content: Center(
            child: SizedBox(
              width: 50,
              height: 50,
              child: LinearProgressIndicator(
                backgroundColor: Colors.indigoAccent,
                color: Colors.indigo,
              )
            ),
          ),
        );
      },
    );
  }

  void _showProcessedImageDialog() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          backgroundColor: Colors.white,
          title: const Text(
            'Result',
            style: TextStyle(
              color: Colors.indigo,
              fontWeight: FontWeight.bold,
            ),
          ),
          content: _processedImage == null
              ? const Text('Sem imagem processada.')
              : Container(
                  child: Image.memory(_processedImage!),
                ),
          actions: <Widget>[
            TextButton(
              style: TextButton.styleFrom(
                foregroundColor: Colors.white,
                backgroundColor: Colors.indigo,
              ),
              child: const Text('Close'),
              onPressed: () {
                Navigator.of(context).pop();
                setState(() {
                  _processedImage = null;
                });
              },
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.indigo[300],
      appBar: AppBar(
        title: const Text(
          'Remove Background',
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: Colors.indigo[900],
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              const SizedBox(height: 20),
              if (_image == null)
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.indigo,
                    foregroundColor: Colors.white
                  ),
                  onPressed: _pickImage,
                  child: const Text('Select Image'),
                ),
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.indigoAccent,
                    foregroundColor: Colors.white
                  ),
                  onPressed: _pickImageFromCamera,
                  child: const Text('Capture Image'),
                ),
              if (_image != null)
                Container(
                  width: 300,
                  height: 300,
                  child: Image.file(_image!),
                ),
              if (_image != null) const SizedBox(height: 20),
              if (_image != null)
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.indigo,
                    foregroundColor: Colors.white
                  ),
                  onPressed: _sendImage,
                  child: const Text('Lets Go!'),
                ),
              if (_processedImage != null) const SizedBox(height: 20),
              if (_processedImage != null)
                Container(
                  width: 300,
                  height: 300,
                  child: Image.memory(_processedImage!),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
