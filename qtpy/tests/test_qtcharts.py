# coding=utf-8
import importlib
from types import ModuleType

import pytest

from qtpy import API_NAME, PYSIDE2, PYSIDE6


@pytest.mark.skipif(
    not (PYSIDE2 or PYSIDE6),
    reason="Only available by default in PySide",
)
def test_qtcharts():
    """Test the qtpy.QtCharts namespace"""
    QtCharts = pytest.importorskip("qtpy.QtCharts")

    assert QtCharts.QChart is not None
    assert QtCharts.QtCharts.QChart is not None


@pytest.mark.skipif(
    not (PYSIDE2 or PYSIDE6),
    reason="Only available by default in PySide",
)
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtCharts")
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace('qtpy', API_NAME)
    )

    extra_members = (
        frozenset(object.__dir__(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ]
        )
        - frozenset(
            # The module is imported from within itself.
            [
                "QtCharts",
            ]
        )
        - frozenset(
            # These don't show up in `dir()` when on PySide:
            dir(object)
            + [
                "QAbstractAxis",
                "QAbstractBarSeries",
                "QAbstractSeries",
                "QAreaLegendMarker",
                "QAreaSeries",
                "QBarCategoryAxis",
                "QBarLegendMarker",
                "QBarModelMapper",
                "QBarSeries",
                "QBarSet",
                "QBoxPlotLegendMarker",
                "QBoxPlotModelMapper",
                "QBoxPlotSeries",
                "QBoxSet",
                "QCandlestickLegendMarker",
                "QCandlestickModelMapper",
                "QCandlestickSeries",
                "QCandlestickSet",
                "QCategoryAxis",
                "QChart",
                "QChartView",
                "QDateTimeAxis",
                "QHBarModelMapper",
                "QHBoxPlotModelMapper",
                "QHCandlestickModelMapper",
                "QHPieModelMapper",
                "QHXYModelMapper",
                "QHorizontalBarSeries",
                "QHorizontalPercentBarSeries",
                "QHorizontalStackedBarSeries",
                "QLegend",
                "QLegendMarker",
                "QLineSeries",
                "QLogValueAxis",
                "QPercentBarSeries",
                "QPieLegendMarker",
                "QPieModelMapper",
                "QPieSeries",
                "QPieSlice",
                "QPolarChart",
                "QScatterSeries",
                "QSplineSeries",
                "QStackedBarSeries",
                "QVBarModelMapper",
                "QVBoxPlotModelMapper",
                "QVCandlestickModelMapper",
                "QVPieModelMapper",
                "QVXYModelMapper",
                "QValueAxis",
                "QXYLegendMarker",
                "QXYModelMapper",
                "QXYSeries",
                "__annotations__",
                "__dict__",
                "__module__",
            ]
        )
    )
    assert not extra_members
