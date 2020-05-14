import 'package:flutter/material.dart';
import 'package:intl/intl.dart'; //package for formatting date to more human redable format

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
        id: 't3', title: "something", amount: 555.00, date: DateTime.now()),
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
        //main axis top to bottom alignment
        //mainAxisAlignment: MainAxisAlignment.spaceAround,
        //cross axis left to right alignment
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: <Widget>[
          Container(
              width: double.infinity,
              child: Card(
                color: Colors.blue,
                child: Text('where chart will go!'),
                elevation: 5,
              )),
          Card(
              elevation: 5,
              child: Container(
                padding: EdgeInsets.all(10),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: <Widget>[
                    TextField(decoration: InputDecoration(labelText: "Ttitle"),),
                    TextField(decoration: InputDecoration(labelText: "Amount"),),
                    FlatButton(child: Text("add transaction"),
                    textColor: Colors.green,
                    onPressed: () {},)
                  ],
                ),
              )),
          //dynamic rendering mapping lists
          Column(
            children: transactions.map((transaction) {
              return Card(
                  child: Row(children: <Widget>[
                Container(
                    margin: EdgeInsets.symmetric(
                      vertical: 15,
                      horizontal: 15,
                    ),
                    decoration: BoxDecoration(
                        border: Border.all(
                      color: Colors.purple,
                      width: 2,
                    )),
                    padding: EdgeInsets.all(10),
                    child: Text("\$${transaction.amount.toString()}",
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 20,
                          color: Colors.purple,
                        ))),
                Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: <Widget>[
                      Text(transaction.title,
                          style: TextStyle(fontWeight: FontWeight.bold)),
                      Text(DateFormat.yMMMd().format(transaction.date),
                          style: TextStyle(color: Colors.grey)),
                      Text("sample text"),
                      Text("another sample text")
                    ])
              ]));
            }).toList(),
          )
        ],
      ),
    );
  }
}
