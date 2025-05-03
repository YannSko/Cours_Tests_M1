import pytest
import numpy as np
from calculate.operators import Operators

class TestOperators:
    """Tests pour le module Operators."""

    @pytest.fixture
    def operator(self):
        """Fixture pour créer une instance de Operators."""
        return Operators()

    # Tests des opérations de base
    def test_addition(self, operator):
        """Test de l'addition."""
        assert operator.addition("2 + 3") == 5
        assert operator.addition("-1 + 1") == 0
        assert operator.addition("2.5 + 3.5") == 6.0
        assert operator.addition("0 + 0") == 0
        assert operator.addition("-2 + -3") == -5
        with pytest.raises(ValueError):
            operator.addition("2 + a")

    def test_substraction(self, operator):
        """Test de la soustraction."""
        assert operator.substraction("5 - 3") == 2
        assert operator.substraction("1 - 1") == 0
        assert operator.substraction("2.5 - 1.5") == 1.0
        assert operator.substraction("0 - 0") == 0
        assert operator.substraction("-2 - -3") == 1
        with pytest.raises(ValueError):
            operator.substraction("2 - a")

    def test_multiplication(self, operator):
        """Test de la multiplication."""
        assert operator.multiplication("2 * 3") == 6
        assert operator.multiplication("-2 * 3") == -6
        assert operator.multiplication("2.5 * 2") == 5.0
        assert operator.multiplication("0 * 5") == 0
        assert operator.multiplication("-2 * -3") == 6
        with pytest.raises(ValueError):
            operator.multiplication("2 * a")

    def test_division(self, operator):
        """Test de la division."""
        assert operator.division("6 / 2") == 3
        assert operator.division("5 / 2") == 2.5
        assert operator.division("-6 / 2") == -3
        assert operator.division("0 / 5") == 0
        with pytest.raises(ValueError):
            operator.division("5 / 0")
        with pytest.raises(ValueError):
            operator.division("2 / a")

    def test_power(self, operator):
        """Test de la puissance."""
        assert operator.power("2 ^ 3") == 8
        assert operator.power("2 ^ 0") == 1
        assert operator.power("2 ^ -1") == 0.5
        assert operator.power("0 ^ 5") == 0
        assert operator.power("-2 ^ 2") == 4
        with pytest.raises(ValueError):
            operator.power("2 ^ a")

    def test_square_root(self, operator):
        """Test de la racine carrée."""
        assert operator.square_root("sqrt(16)") == 4
        assert operator.square_root("sqrt(2)") == pytest.approx(1.4142135623730951)
        assert operator.square_root("sqrt(0)") == 0
        with pytest.raises(ValueError):
            operator.square_root("sqrt(-1)")
        with pytest.raises(ValueError):
            operator.square_root("sqrt(a)")

    def test_logarithm(self, operator):
        """Test du logarithme."""
        assert operator.logarithm("log(1)") == 0
        assert operator.logarithm("log(2.718281828459045)") == pytest.approx(1)
        with pytest.raises(ValueError):
            operator.logarithm("log(0)")
        with pytest.raises(ValueError):
            operator.logarithm("log(-1)")
        with pytest.raises(ValueError):
            operator.logarithm("log(a)")

    def test_modulo(self, operator):
        """Test du modulo."""
        assert operator.modulo("5 % 2") == 1
        assert operator.modulo("10 % 3") == 1
        assert operator.modulo("0 % 5") == 0
        with pytest.raises(ValueError):
            operator.modulo("5 % 0")
        with pytest.raises(ValueError):
            operator.modulo("2 % a")

    def test_trigonometric_functions(self, operator):
        """Test des fonctions trigonométriques."""
        assert operator.sine("sin(0)") == 0
        assert operator.sine("sin(3.14159)") == pytest.approx(0)
        assert operator.cosine("cos(0)") == 1
        assert operator.cosine("cos(3.14159)") == pytest.approx(-1)
        assert operator.tangent("tan(0)") == 0
        with pytest.raises(ValueError):
            operator.sine("sin(a)")
        with pytest.raises(ValueError):
            operator.cosine("cos(a)")
        with pytest.raises(ValueError):
            operator.tangent("tan(a)")

    def test_factorial(self, operator):
        """Test de la factorielle."""
        assert operator.factorial("5!") == 120
        assert operator.factorial("0!") == 1
        with pytest.raises(ValueError):
            operator.factorial("-1!")
        with pytest.raises(ValueError):
            operator.factorial("a!")

    def test_absolute(self, operator):
        """Test de la valeur absolue."""
        assert operator.absolute("abs(-5)") == 5
        assert operator.absolute("abs(5)") == 5
        assert operator.absolute("abs(0)") == 0
        with pytest.raises(ValueError):
            operator.absolute("abs(a)")

    def test_exponential(self, operator):
        """Test de l'exponentielle."""
        assert operator.exponential("exp(0)") == 1
        assert operator.exponential("exp(1)") == pytest.approx(2.718281828459045)
        with pytest.raises(ValueError):
            operator.exponential("exp(a)")

    # Tests des fonctions statistiques
    def test_mean(self, operator):
        """Test de la moyenne."""
        assert operator.mean("mean(1,2,3,4,5)") == 3
        assert operator.mean("mean(2.5,3.5)") == 3.0
        assert operator.mean("mean(0,0,0)") == 0
        with pytest.raises(ValueError):
            operator.mean("mean(1,a,3)")

    def test_median(self, operator):
        """Test de la médiane."""
        assert operator.median("median(1,2,3,4,5)") == 3
        assert operator.median("median(1,2,3,4)") == 2.5
        assert operator.median("median(0,0,0)") == 0
        with pytest.raises(ValueError):
            operator.median("median(1,a,3)")

    def test_mode(self, operator):
        """Test du mode."""
        assert operator.mode("mode(1,2,2,3,3,3)") == 3
        assert operator.mode("mode(1,1,2,2)") == 1
        assert operator.mode("mode(0,0,0)") == 0
        with pytest.raises(ValueError):
            operator.mode("mode(1,a,3)")

    def test_standard_deviation(self, operator):
        """Test de l'écart-type."""
        assert operator.standard_deviation("std(1,2,3,4,5)") == pytest.approx(1.4142135623730951)
        assert operator.standard_deviation("std(0,0,0)") == 0
        with pytest.raises(ValueError):
            operator.standard_deviation("std(1,a,3)")

    def test_variance(self, operator):
        """Test de la variance."""
        assert operator.variance("var(1,2,3,4,5)") == pytest.approx(2.0)
        assert operator.variance("var(0,0,0)") == 0
        with pytest.raises(ValueError):
            operator.variance("var(1,a,3)")

    def test_percentile(self, operator):
        """Test du percentile."""
        assert operator.percentile("percentile(1,2,3,4,5;50)") == 3
        assert operator.percentile("percentile(1,2,3,4,5;75)") == 4
        with pytest.raises(ValueError):
            operator.percentile("percentile(1,2,3;150)")
        with pytest.raises(ValueError):
            operator.percentile("percentile(1,a,3;50)")

    def test_correlation(self, operator):
        """Test de la corrélation."""
        assert operator.correlation("correlation(1,2,3;4,5,6)") == pytest.approx(1.0)
        assert operator.correlation("correlation(1,2,3;6,5,4)") == pytest.approx(-1.0)
        with pytest.raises(ValueError):
            operator.correlation("correlation(1,2;4,5,6)")
        with pytest.raises(ValueError):
            operator.correlation("correlation(1,a,3;4,5,6)")

    def test_linear_regression(self, operator):
        """Test de la régression linéaire."""
        result = operator.linear_regression("regression(1,2,3;4,5,6)")
        assert result['slope'] == pytest.approx(1.0)
        assert result['intercept'] == pytest.approx(3.0)
        assert result['r_squared'] == pytest.approx(1.0)
        with pytest.raises(ValueError):
            operator.linear_regression("regression(1,2;4,5,6)")
        with pytest.raises(ValueError):
            operator.linear_regression("regression(1,a,3;4,5,6)")

    # Tests des fonctions de visualisation
    def test_plot_function(self, operator):
        """Test du tracé de fonction."""
        result = operator.plot_function("plot(x^2, -10, 10)")
        assert "Graphique sauvegardé" in result
        with pytest.raises(ValueError):
            operator.plot_function("plot(x^2, a, 10)")

    def test_scatter_plot(self, operator):
        """Test du nuage de points."""
        result = operator.scatter_plot("scatter(1,2,3,4)")
        assert "Graphique sauvegardé" in result
        with pytest.raises(ValueError):
            operator.scatter_plot("scatter(1,a,3,4)")

    def test_histogram(self, operator):
        """Test de l'histogramme."""
        result = operator.histogram("histogram(1,2,2,3,3,3)")
        assert "Graphique sauvegardé" in result
        with pytest.raises(ValueError):
            operator.histogram("histogram(1,a,3)")

    def test_polar_plot(self, operator):
        """Test du graphique polaire."""
        result = operator.polar_plot("polar(2*sin(theta), 0, 6.28)")
        assert "Graphique sauvegardé" in result
        with pytest.raises(ValueError):
            operator.polar_plot("polar(2*sin(theta), a, 6.28)")

    def test_plot_3d(self, operator):
        """Test du graphique 3D."""
        result = operator.plot_3d("3d(x^2+y^2, -2, 2, -2, 2)")
        assert "Graphique sauvegardé" in result
        with pytest.raises(ValueError):
            operator.plot_3d("3d(x^2+y^2, a, 2, -2, 2)")

    def test_boxplot(self, operator):
        """Test du diagramme en boîte."""
        result = operator.boxplot("boxplot(1,2,2,3,3,3,4,4,5)")
        assert "Graphique sauvegardé" in result
        with pytest.raises(ValueError):
            operator.boxplot("boxplot(1,a,3)")

    def test_qqplot(self, operator):
        """Test du graphique Q-Q."""
        result = operator.qqplot("qqplot(1,2,3,4,5)")
        assert "Graphique sauvegardé" in result
        with pytest.raises(ValueError):
            operator.qqplot("qqplot(1,a,3)")

    def test_heatmap(self, operator):
        """Test de la carte de chaleur."""
        result = operator.heatmap("heatmap(1,2,3;4,5,6)")
        assert "Graphique sauvegardé" in result
        with pytest.raises(ValueError):
            operator.heatmap("heatmap(1,a,3;4,5,6)")

    def test_pie_chart(self, operator):
        """Test du diagramme circulaire."""
        result = operator.pie_chart("pie(30,20,50;A,B,C)")
        assert "Graphique sauvegardé" in result
        with pytest.raises(ValueError):
            operator.pie_chart("pie(30,a,50;A,B,C)")

    def test_bar_chart(self, operator):
        """Test du diagramme en barres."""
        result = operator.bar_chart("bar(10,20,30;A,B,C)")
        assert "Graphique sauvegardé" in result
        with pytest.raises(ValueError):
            operator.bar_chart("bar(10,a,30;A,B,C)")

    # Tests des fonctions de parsing
    def test_parse_list(self, operator):
        """Test du parsing de liste."""
        assert operator._parse_list("mean(1,2,3)", "mean") == [1.0, 2.0, 3.0]
        with pytest.raises(ValueError):
            operator._parse_list("mean(1,a,3)", "mean")
        with pytest.raises(ValueError):
            operator._parse_list("mean()", "mean")

    def test_parse_two_lists(self, operator):
        """Test du parsing de deux listes."""
        list1, list2 = operator._parse_two_lists("correlation(1,2,3;4,5,6)", "correlation")
        assert list1 == [1.0, 2.0, 3.0]
        assert list2 == [4.0, 5.0, 6.0]
        with pytest.raises(ValueError):
            operator._parse_two_lists("correlation(1,2,3)", "correlation")
        with pytest.raises(ValueError):
            operator._parse_two_lists("correlation(1,a,3;4,5,6)", "correlation")

    def test_parse_matrix(self, operator):
        """Test du parsing de matrice."""
        matrix = operator._parse_matrix("heatmap(1,2,3;4,5,6)", "heatmap")
        assert matrix.shape == (2, 3)
        assert matrix[0, 0] == 1.0
        assert matrix[1, 2] == 6.0
        with pytest.raises(ValueError):
            operator._parse_matrix("heatmap(1,a,3;4,5,6)", "heatmap")
        with pytest.raises(ValueError):
            operator._parse_matrix("heatmap(1,2,3)", "heatmap")

    def test_parse_pie_data(self, operator):
        """Test du parsing des données pour le diagramme circulaire."""
        values, labels = operator._parse_pie_data("pie(30,20,50;A,B,C)")
        assert values == [30.0, 20.0, 50.0]
        assert labels == ["A", "B", "C"]
        with pytest.raises(ValueError):
            operator._parse_pie_data("pie(30,20;A,B,C)")
        with pytest.raises(ValueError):
            operator._parse_pie_data("pie(30,a,50;A,B,C)")

    def test_parse_bar_data(self, operator):
        """Test du parsing des données pour le diagramme en barres."""
        values, labels = operator._parse_bar_data("bar(10,20,30;A,B,C)")
        assert values == [10.0, 20.0, 30.0]
        assert labels == ["A", "B", "C"]
        with pytest.raises(ValueError):
            operator._parse_bar_data("bar(10,20;A,B,C)")
        with pytest.raises(ValueError):
            operator._parse_bar_data("bar(10,a,30;A,B,C)")

    def test_parse_operation_with_percentile(self, operator):
        """Test du parsing d'opération avec percentile."""
        values, p = operator._parse_operation_with_percentile("percentile(1,2,3,4,5;75)", "percentile")
        assert values == [1.0, 2.0, 3.0, 4.0, 5.0]
        assert p == 75.0
        with pytest.raises(ValueError):
            operator._parse_operation_with_percentile("percentile(1,2,3;150)", "percentile")
        with pytest.raises(ValueError):
            operator._parse_operation_with_percentile("percentile(1,a,3;50)", "percentile") 