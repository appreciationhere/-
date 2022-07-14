#include "wait.h"
#include "ui_wait.h"
#include "QTimer"
#include "QFile"
#include "QProcess"
short cnt1 = 0;
extern QProcess* p1 ;
extern QProcess* p2 ;
wait::wait(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::wait)
{
    p1->close();
    p2->start("./regsiter.sh");
    ui->setupUi(this);
    QTimer* time = new QTimer(this);
    time->start(2000);
    connect(time, &QTimer::timeout, [=]() {
        QByteArray arry;
        QFile afile("1.txt");
        afile.open(QIODevice::ReadOnly);
        arry = afile.readAll();
        afile.close();
        if (arry[0]== '0') {
            ui->label->setText("认证成功");
            p2->close();
        }
        if (cnt1 == 30) {
            ui->label->setText("time too long...");
            p2->close();
        }
        cnt1++;
    });
}

wait::~wait()
{
    delete ui;
}
