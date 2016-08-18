def introduce_renamed_methods_qheaderview(QHeaderView):

    def sectionsClickable(self):
        """
        QHeaderView.sectionsClickable() -> bool
        """
        return QHeaderView.isClickable(self)
    QHeaderView.sectionsClickable = sectionsClickable

    def sectionsMovable(self):
        """
        QHeaderView.sectionsMovable() -> bool
        """
        return QHeaderView.isMovable(self)
    QHeaderView.sectionsMovable = sectionsMovable

    def sectionResizeMode(self, logicalIndex):
        """
        QHeaderView.sectionResizeMode(int) -> QHeaderView.ResizeMode
        """
        return QHeaderView.resizeMode(self, logicalIndex)
    QHeaderView.sectionResizeMode = sectionResizeMode

    def setSectionsClickable(self, clickable):
        """
        QHeaderView.setSectionsClickable(bool)
        """
        return QHeaderView.setClickable(self, clickable)
    QHeaderView.setSectionsClickable = setSectionsClickable

    def setSectionsMovable(self, movable):
        """
        QHeaderView.setSectionsMovable(bool)
        """
        return QHeaderView.setMovable(self, movable)
    QHeaderView.setSectionsMovable = setSectionsMovable

    def setSectionResizeMode(self, *args):
        """
        QHeaderView.setSectionResizeMode(QHeaderView.ResizeMode)
        QHeaderView.setSectionResizeMode(int, QHeaderView.ResizeMode)
        """
        QHeaderView.setResizeMode(self, *args)
    QHeaderView.setSectionResizeMode = setSectionResizeMode




