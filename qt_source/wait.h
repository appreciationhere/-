#ifndef WAIT_H
#define WAIT_H

#include <QWidget>

namespace Ui {
class wait;
}

class wait : public QWidget
{
    Q_OBJECT

public:
    explicit wait(QWidget *parent = nullptr);
    ~wait();

private:
    Ui::wait *ui;
};

#endif // WAIT_H
