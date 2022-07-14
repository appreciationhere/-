#ifndef INPUT_H
#define INPUT_H

#include <QWidget>

namespace Ui {
class Input;
}

class Input : public QWidget
{
    Q_OBJECT

public:
    explicit Input(QWidget *parent = nullptr);
    ~Input();

private slots:
    void on_pushButton_clicked();

private:
    Ui::Input *ui;
};

#endif // INPUT_H
