/********************************************************************************
** Form generated from reading UI file 'wait.ui'
**
** Created by: Qt User Interface Compiler version 5.11.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WAIT_H
#define UI_WAIT_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_wait
{
public:
    QLabel *label;

    void setupUi(QWidget *wait)
    {
        if (wait->objectName().isEmpty())
            wait->setObjectName(QStringLiteral("wait"));
        wait->resize(324, 131);
        label = new QLabel(wait);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(30, 50, 251, 31));
        QFont font;
        font.setPointSize(15);
        label->setFont(font);

        retranslateUi(wait);

        QMetaObject::connectSlotsByName(wait);
    } // setupUi

    void retranslateUi(QWidget *wait)
    {
        wait->setWindowTitle(QApplication::translate("wait", "Form", nullptr));
        label->setText(QApplication::translate("wait", "\350\257\267\351\235\242\345\220\221\346\221\204\345\203\217\345\244\264\350\277\233\350\241\214\345\233\276\345\203\217\351\207\207\351\233\206", nullptr));
    } // retranslateUi

};

namespace Ui {
    class wait: public Ui_wait {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WAIT_H
