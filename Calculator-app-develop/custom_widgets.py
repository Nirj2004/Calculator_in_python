from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *




class PushButton(QPushButton):
    BASE_COLOR = '#202020'
    HOVER_COLOR = '#505050'
    PRESS_COLOR = '#707070'

    def __init__(self, basecolor=BASE_COLOR, hovercolor=HOVER_COLOR, presscolor=PRESS_COLOR):
        super(PushButton, self). __init__()
        self._animation1 = QVariantAnimation(
            startValue=QColor(hovercolor),
            endValue=QColor(basecolor),
            valueChanged=self._on_value_changed,
            duration=200,
        )
        self._animation2 = QVariantAnimation(
            startValue=QColor(presscolor),
            endValue=QColor(hovercolor),
            valueChanged=self._on_value_changed,
            duration=120,
        )


        self._update_stylesheet((QColor(basecolor)) # passing in default background color
        # self.setCursor(Qt.PointingHandCursor)
        
    def _on_value_changed(self, color):
        self._update_StyleSheet(
            f"""
            front-weight: normal;
            min-width: 64px;
            min-height: 70px;
            margin: -5px;
            background-color: {background.name()};
            """
        )

    def enterEvent(self, event, *args, **kwargs):
        self._animation1.setDirection(QAbstractAnimation.Backward)
        self.animation1.start()
        super().enterEvent(event)

    def leaveEvent(self, event, *args, **kwargs):
        self._animation1.setDirection(QAbstractAnimation.Forward)
        self.animation1.start()
        super().leaveEvent(event)

    def mousePressEvent(self, event, *args, **kwargs):
        self._animation2.setDirection(QAbstractAnimation.Backward)
        self._animation2.start()
        super(PushButton, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event, *args, **kwargs):
        self._animation2.setDirection(QAbstractAnimstion.Forward)
        self._animation2.start()
        super(PushButton, self).mouseReleaseEvent(event)

class NoCursorLineEdit(QLineEdit):

    def __init__(self):
        super(NoCursorLineEdit, self).__init__()
        self.setReadyOnly(True)

    def paintEvent(self, event): # setting blinking cursor color to same as background color to hide it...lol big brain('_')
        super(NoCursorLineEdit, self).paintEvent(event)
        rect = self.cursorRect()
        painter = QPainter(self)
        new_rect = QRect(rect.x() + (rect.width() / 2), rect.y(), rect.width() - rect.width() * 0.8), rect.height())
        painter.fillRect(new_rect, QColor('#353535'))


class BlurEffect(QGraphicsBlurEffect):
    effectRect = None
    
    def setEffectRect(self, rect):
        self.effectRect = rect
        self.update()


    def draw(self, qp):
        if self.effectRect is None or self.effectRect.isNull():
            # no valid effect rect to be used, use the default implementation
            super().draw(qp)
            print('bao')
        else:
            qp.save()
            # clip the drawing so that it's restricted to the effectRect
            qp.setClipRect(self.effectRect)
            # call the default implementation, which will draw the effect
            super().draw(qp)
            # get the full region that should be painted
            fullRegion = QRegion(qp.viewport())
            # and subtract the effect rectangle
            fullRegion -= QRegion(self.effectRect)
            qp.setClipRegion(fullRegion)
            # draw the *source*, which has no effect applied
            self.drawSource(qp)
            qp.restore()



class HSeparationLine(QFrame):
    """
      Custom Class to create a horizontal separation line.
    """
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(1)
        self.setFixedHeight(1)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.sunken)
        self.setSizePolicy(QSizePolicy.Preffered, QSizePolicy.Minimum)
        return



# WILL NEED WAYYY EXTRA CHECKS AND LOGIC TO SYNC IT WITH BUTTON FUNCTIONS - maybe do later 💀
# class NumberInputValidator(QValidator):
#     """
#     Custom validator class to validate number input in Calc screen.
#     """
#
#     def validate(self, v_string: str, index: int):
#         # invalid_chars =
#         # `~!@#$%^&*()-_=+{[}]|\\'",<>/?
#         state = None
#         if len(v_string) < 1 or v_string[:1] != '0':
#             # ic('Less than 2 or not 0 - invalid')
#             state = QValidator.Invalid
#
#         if len(v_string) >= 1:
#             # ic('Greater than 1 - VALID')
#             state = QValidator.Intermediate
#
#         if (v_string[:].isdigit()) is True:
#             # ic('All digits - VALID')
#             state = QValidator.Acceptable
#
#         for x in v_string[:]:
#             if ((x.isdigit() is False) and '.' not in v_string[:]) or x.isalpha():
#                 # ic('Alpha or Anything else - invalid')
#                 state = QValidator.Invalid
#
#         nums = v_string[:].split('.')
#         if '.' in v_string[:]:
#             if (nums[0].isdigit() and nums[1].isdigit()) is True:
#                 # ic('Has period and both numbers are legit - VALID')
#                 state = QValidator.Acceptable
#             if '.' in v_string[:] and len(v_string.split('.')[1]) >= 1:
#                 if (nums[0].isdigit() is True) and (nums[1].isdigit() is False):
#                     # ic('Has period, but other chars too - invalid')
#                     state = QValidator.Invalid
#             if len(nums[1]) > 2:
#                 # ic('More than 2 digits after period - invalid')
#                 state = QValidator.Invalid
#
#         if v_string.count('.') > 1:
#             # ic('More than one period - invalid')
#             state = QValidator.Invalid
#
#         return state, v_string, index



# THIS BREAKS MY APPS UI - It's supposed to realign button icons with text.
# class ProxyStyle(QProxyStyle):
#     def drawControl(self, element, option, painter, widget=None):
#         if element == QStyle.CE_PushButtonLabel:
#             icon = QIcon(option.icon)
#             option.icon = QIcon()
#         super(ProxyStyle, self).drawControl(element, option, painter, widget)
#         if element == QStyle.CE_PushButtonLabel:
#             if not icon.isNull():
#                 iconSpacing = 4
#                 mode = (
#                     QIcon.Normal
#                     if option.state & QStyle.State_Enabled
#                     else QIcon.Disabled
#                 )
#                 if (
#                     mode == QIcon.Normal
#                     and option.state & QStyle.State_HasFocus
#                 ):
#                     mode = QIcon.Active
#                 state = QIcon.Off
#                 if option.state & QStyle.State_On:
#                     state = QIcon.On
#                 window = widget.window().windowHandle() if widget is not None else None
#                 pixmap = icon.pixmap(window, option.iconSize, mode, state)
#                 pixmapWidth = pixmap.width() / pixmap.devicePixelRatio()
#                 pixmapHeight = pixmap.height() / pixmap.devicePixelRatio()
#                 iconRect = QRect(
#                     QPoint(), QSize(pixmapWidth, pixmapHeight)
#                 )
#                 iconRect.moveCenter(option.rect.center())
#                 iconRect.moveLeft(option.rect.left() + iconSpacing)
#                 iconRect = self.visualRect(option.direction, option.rect, iconRect)
#                 iconRect.translate(
#                     self.proxy().pixelMetric(
#                         QStyle.PM_ButtonShiftHorizontal, option, widget
#                     ),
#                     self.proxy().pixelMetric(
#                         QStyle.PM_ButtonShiftVertical, option, widget
#                     ),
#                 )
#                 painter.drawPixmap(iconRect, pixmap)



