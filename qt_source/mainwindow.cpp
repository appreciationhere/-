#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "wait.h"
#include "QProcess"
#include "input.h"
QProcess* p1 = new QProcess();
QProcess* p2 = new QProcess();
QProcess* p3 = new QProcess();
wait* wait1 = nullptr;
Input* input = nullptr;
extern QString  name;
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
    p1->close();
    p2->close();
    delete wait1;
    delete p1;
    delete p2;
}

void MainWindow::on_pushButton_4_clicked()
{
    p1->close();
    p3->start("./pkill.sh");
    input = new Input();
    input->show();
}

void MainWindow::on_pushButton_2_clicked()
{
    p1->start("./reg.sh");
}

void MainWindow::on_pushButton_3_clicked()
{
    p1->close();
    p3->start("./pkill.sh");
}
