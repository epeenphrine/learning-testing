import 'package:flutter/material.dart';
import './transaction.dart';

// flutter is built by using widgets Text, Button, and etc.. are all widgets
void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  //create a list of transcations
  final List<Transaction> transactions = [
    Transaction(
        id: 't1', title: "new shoes", amount: 420.00, date: DateTime.now()),
    Transaction(
        id: "t2", title: "gucci belt", amount: 69.00, date: DateTime.now())
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Flutter App'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: <Widget>[
          Container(
              width: double.infinity,
              child: Card(
                color: Colors.blue,
                child: Text('CHART!'),
                elevation: 5,
              )),
          //dynamic rendering mapping lists
          Column(
            children: transactions.map((transaction) {
              return Card(
                  child: Row(children: <Widget>[
                Container(child: Text(transaction.amount.toString())),
                Column(children: <Widget>[
                    Text(transaction.title),
                    Text(transaction.date.toString())
                ])
              ]));
            }).toList(),
          )
        ],
      ),
    );
  }
}
