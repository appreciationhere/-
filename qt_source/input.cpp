#include "input.h"
#include "ui_input.h"
#include "wait.h"
#include "QFile"
QString name = "";
using namespace std;
extern wait* wait1;
extern Input* input;
Input::Input(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Input)
{
    ui->setupUi(this);
}

Input::~Input()
{
    delete ui;
}

void Input::on_pushButton_clicked()
{
    name = ui->textEdit->toPlainText();
    QFile afile("1.txt");
    afile.open(QIODevice::WriteOnly | QIODevice::Text);
    QByteArray strb= name.toUtf8();
    afile.write(strb, strb.length());
    afile.close();
    wait1 = new wait();
    input->close();
    wait1->show();
}
