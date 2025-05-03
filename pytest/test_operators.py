import pytest
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock
from calculate.operators import Operators

@pytest.fixture
def operators():
    """Fixture pour créer une instance d'Operators."""
    return Operators()

class TestOperators:
    """Tests pour la classe Operators."""
    
    def test_init(self, operators):
        """Test l'initialisation des opérateurs."""
        assert isinstance(operators, Operators)
    
    def test_setup_visualization(self, operators):
        """Test la configuration de la visualisation."""
        with patch('matplotlib.pyplot.style.use') as mock_style:
            operators._setup_visualization()
            mock_style.assert_called_once_with('seaborn')
    
    def test_validate_numeric_input(self, operators):
        """Test la validation des entrées numériques."""
        # Cas valides
        assert operators._validate_numeric_input(5) == 5.0
        assert operators._validate_numeric_input("3.14") == 3.14
        assert operators._validate_numeric_input(-10) == -10.0
        
        # Cas invalides
        with pytest.raises(ValueError):
            operators._validate_numeric_input("abc")
        with pytest.raises(ValueError):
            operators._validate_numeric_input(None)
    
    def test_validate_list_input(self, operators):
        """Test la validation des entrées de liste."""
        # Cas valides
        assert operators._validate_list_input([1, 2, 3]) == [1.0, 2.0, 3.0]
        assert operators._validate_list_input("1.5, 2.5, 3.5") == [1.5, 2.5, 3.5]
        
        # Cas invalides
        with pytest.raises(ValueError):
            operators._validate_list_input([])
        with pytest.raises(ValueError):
            operators._validate_list_input([1, "abc", 3])
        with pytest.raises(ValueError):
            operators._validate_list_input(None)
    
    def test_validate_matrix_input(self, operators):
        """Test la validation des entrées de matrice."""
        # Cas valides
        assert operators._validate_matrix_input([[1, 2], [3, 4]]) == [[1.0, 2.0], [3.0, 4.0]]
        assert operators._validate_matrix_input("1, 2; 3, 4") == [[1.0, 2.0], [3.0, 4.0]]
        
        # Cas invalides
        with pytest.raises(ValueError):
            operators._validate_matrix_input([])
        with pytest.raises(ValueError):
            operators._validate_matrix_input([[1, 2], [3]])
        with pytest.raises(ValueError):
            operators._validate_matrix_input([[1, "abc"], [3, 4]])
        with pytest.raises(ValueError):
            operators._validate_matrix_input(None)
    
    def test_addition(self, operators):
        """Test l'addition."""
        assert operators.addition("2 + 3") == 5
        assert operators.addition("-1 + 1") == 0
        assert operators.addition("2.5 + 3.5") == 6.0
        
        with pytest.raises(ValueError):
            operators.addition("2 + a")
    
    def test_substraction(self, operators):
        """Test la soustraction."""
        assert operators.substraction("5 - 3") == 2
        assert operators.substraction("1 - 1") == 0
        assert operators.substraction("5.5 - 2.5") == 3.0
        
        with pytest.raises(ValueError):
            operators.substraction("5 - a")
    
    def test_multiplication(self, operators):
        """Test la multiplication."""
        assert operators.multiplication("2 * 3") == 6
        assert operators.multiplication("-2 * 3") == -6
        assert operators.multiplication("2.5 * 2") == 5.0
        
        with pytest.raises(ValueError):
            operators.multiplication("2 * a")
    
    def test_division(self, operators):
        """Test la division."""
        assert operators.division("6 / 2") == 3
        assert operators.division("5 / 2") == 2.5
        
        with pytest.raises(ValueError):
            operators.division("5 / 0")
        with pytest.raises(ValueError):
            operators.division("5 / a")
    
    def test_power(self, operators):
        """Test la puissance."""
        assert operators.power("2 ^ 3") == 8
        assert operators.power("2 ^ 0") == 1
        assert operators.power("2 ^ -1") == 0.5
        
        with pytest.raises(ValueError):
            operators.power("2 ^ a")
    
    def test_square_root(self, operators):
        """Test la racine carrée."""
        assert operators.square_root("16") == 4
        assert pytest.approx(operators.square_root("2"), 0.0001) == 1.4142
        
        with pytest.raises(ValueError):
            operators.square_root("-1")
        with pytest.raises(ValueError):
            operators.square_root("a")
    
    def test_logarithm(self, operators):
        """Test le logarithme."""
        assert operators.logarithm("1") == 0
        assert pytest.approx(operators.logarithm(str(np.e)), 0.0001) == 1
        
        with pytest.raises(ValueError):
            operators.logarithm("0")
        with pytest.raises(ValueError):
            operators.logarithm("-1")
        with pytest.raises(ValueError):
            operators.logarithm("a")
    
    def test_modulo(self, operators):
        """Test le modulo."""
        assert operators.modulo("5 % 2") == 1
        assert operators.modulo("10 % 3") == 1
        
        with pytest.raises(ValueError):
            operators.modulo("5 % 0")
        with pytest.raises(ValueError):
            operators.modulo("5 % a")
    
    def test_sine(self, operators):
        """Test le sinus."""
        assert operators.sine("0") == 0
        assert pytest.approx(operators.sine(str(np.pi/2)), 0.0001) == 1
        
        with pytest.raises(ValueError):
            operators.sine("a")
    
    def test_cosine(self, operators):
        """Test le cosinus."""
        assert operators.cosine("0") == 1
        assert pytest.approx(operators.cosine(str(np.pi)), 0.0001) == -1
        
        with pytest.raises(ValueError):
            operators.cosine("a")
    
    def test_tangent(self, operators):
        """Test la tangente."""
        assert operators.tangent("0") == 0
        assert pytest.approx(operators.tangent(str(np.pi/4)), 0.0001) == 1
        
        with pytest.raises(ValueError):
            operators.tangent("a")
    
    def test_factorial(self, operators):
        """Test la factorielle."""
        assert operators.factorial("5") == 120
        assert operators.factorial("0") == 1
        
        with pytest.raises(ValueError):
            operators.factorial("-1")
        with pytest.raises(ValueError):
            operators.factorial("3.5")
        with pytest.raises(ValueError):
            operators.factorial("a")
    
    def test_absolute(self, operators):
        """Test la valeur absolue."""
        assert operators.absolute("-5") == 5
        assert operators.absolute("5") == 5
        assert operators.absolute("0") == 0
        
        with pytest.raises(ValueError):
            operators.absolute("a")
    
    def test_exponential(self, operators):
        """Test l'exponentielle."""
        assert operators.exponential("0") == 1
        assert pytest.approx(operators.exponential("1"), 0.0001) == np.e
        assert pytest.approx(operators.exponential("2"), 0.0001) == np.e**2
        
        with pytest.raises(ValueError):
            operators.exponential("a")
    
    def test_mean(self, operators):
        """Test la moyenne."""
        assert operators.mean("1, 2, 3, 4, 5") == 3
        assert operators.mean("2.5, 3.5") == 3.0
        
        with pytest.raises(ValueError):
            operators.mean("")
        with pytest.raises(ValueError):
            operators.mean("1, a, 3")
    
    def test_median(self, operators):
        """Test la médiane."""
        assert operators.median("1, 2, 3, 4, 5") == 3
        assert operators.median("1, 2, 3, 4") == 2.5
        
        with pytest.raises(ValueError):
            operators.median("")
        with pytest.raises(ValueError):
            operators.median("1, a, 3")
    
    def test_mode(self, operators):
        """Test le mode."""
        assert operators.mode("1, 2, 2, 3, 3, 3") == [1.0, 2.0, 3.0]
        
        with pytest.raises(ValueError):
            operators.mode("")
        with pytest.raises(ValueError):
            operators.mode("1, a, 3")
    
    def test_standard_deviation(self, operators):
        """Test l'écart-type."""
        assert pytest.approx(operators.standard_deviation("1, 2, 3, 4, 5"), 0.0001) == np.std([1, 2, 3, 4, 5])
        assert operators.standard_deviation("0, 0, 0") == 0
        
        with pytest.raises(ValueError):
            operators.standard_deviation("")
        with pytest.raises(ValueError):
            operators.standard_deviation("1, a, 3")
    
    def test_variance(self, operators):
        """Test la variance."""
        assert pytest.approx(operators.variance("1, 2, 3, 4, 5"), 0.0001) == np.var([1, 2, 3, 4, 5])
        assert operators.variance("0, 0, 0") == 0
        
        with pytest.raises(ValueError):
            operators.variance("")
        with pytest.raises(ValueError):
            operators.variance("1, a, 3")
    
    def test_percentile(self, operators):
        """Test le percentile."""
        assert operators.percentile("1, 2, 3, 4, 5; 50") == 3
        assert operators.percentile("1, 2, 3, 4, 5; 75") == 4
        
        with pytest.raises(ValueError):
            operators.percentile("; 50")
        with pytest.raises(ValueError):
            operators.percentile("1, 2, 3; -10")
        with pytest.raises(ValueError):
            operators.percentile("1, 2, 3; 110")
        with pytest.raises(ValueError):
            operators.percentile("1, a, 3; 50")
    
    def test_correlation(self, operators):
        """Test la corrélation."""
        assert operators.correlation("1, 2, 3; 4, 5, 6") == 1
        assert operators.correlation("1, 2, 3; 6, 5, 4") == -1
        
        with pytest.raises(ValueError):
            operators.correlation("; 1, 2")
        with pytest.raises(ValueError):
            operators.correlation("1, 2; 1")
        with pytest.raises(ValueError):
            operators.correlation("1, a; 1, 2")
    
    def test_linear_regression(self, operators):
        """Test la régression linéaire."""
        slope, intercept = operators.linear_regression("1, 2, 3; 4, 5, 6")
        assert slope == 1
        assert intercept == 3
        
        with pytest.raises(ValueError):
            operators.linear_regression("; 1, 2")
        with pytest.raises(ValueError):
            operators.linear_regression("1, 2; 1")
        with pytest.raises(ValueError):
            operators.linear_regression("1, a; 1, 2")
    
    @patch('matplotlib.pyplot.savefig')
    def test_plot(self, mock_savefig, operators):
        """Test le traçage de fonction."""
        assert operators.plot("x**2", -10, 10, "test_plot.png") is True
        mock_savefig.assert_called_once_with("test_plot.png")
        
        with pytest.raises(ValueError):
            operators.plot("invalid", -10, 10, "test_plot.png")
    
    @patch('matplotlib.pyplot.savefig')
    def test_scatter(self, mock_savefig, operators):
        """Test le nuage de points."""
        assert operators.scatter([1, 2, 3], [4, 5, 6], "test_scatter.png") is True
        mock_savefig.assert_called_once_with("test_scatter.png")
        
        with pytest.raises(ValueError):
            operators.scatter([], [4, 5, 6], "test_scatter.png")
        with pytest.raises(ValueError):
            operators.scatter([1, 2, 3], [4, 5], "test_scatter.png")
    
    @patch('matplotlib.pyplot.savefig')
    def test_histogram(self, mock_savefig, operators):
        """Test l'histogramme."""
        assert operators.histogram([1, 2, 2, 3, 3, 3], "test_histogram.png") is True
        mock_savefig.assert_called_once_with("test_histogram.png")
        
        with pytest.raises(ValueError):
            operators.histogram([], "test_histogram.png")
    
    @patch('matplotlib.pyplot.savefig')
    def test_polar(self, mock_savefig, operators):
        """Test le graphique polaire."""
        assert operators.polar([0, np.pi/2, np.pi], [1, 2, 3], "test_polar.png") is True
        mock_savefig.assert_called_once_with("test_polar.png")
        
        with pytest.raises(ValueError):
            operators.polar([], [1, 2, 3], "test_polar.png")
        with pytest.raises(ValueError):
            operators.polar([0, np.pi/2, np.pi], [1, 2], "test_polar.png")
    
    @patch('matplotlib.pyplot.savefig')
    def test_plot_3d(self, mock_savefig, operators):
        """Test le graphique 3D."""
        assert operators.plot_3d([1, 2], [3, 4], [5, 6], "test_3d.png") is True
        mock_savefig.assert_called_once_with("test_3d.png")
        
        with pytest.raises(ValueError):
            operators.plot_3d([], [3, 4], [5, 6], "test_3d.png")
        with pytest.raises(ValueError):
            operators.plot_3d([1, 2], [3], [5, 6], "test_3d.png")
        with pytest.raises(ValueError):
            operators.plot_3d([1, 2], [3, 4], [5], "test_3d.png")
    
    @patch('matplotlib.pyplot.savefig')
    def test_boxplot(self, mock_savefig, operators):
        """Test le boxplot."""
        assert operators.boxplot([1, 2, 3, 4, 5], "test_boxplot.png") is True
        mock_savefig.assert_called_once_with("test_boxplot.png")
        
        with pytest.raises(ValueError):
            operators.boxplot([], "test_boxplot.png")
    
    @patch('matplotlib.pyplot.savefig')
    def test_qq_plot(self, mock_savefig, operators):
        """Test le graphique Q-Q."""
        assert operators.qq_plot([1, 2, 3, 4, 5], "test_qq.png") is True
        mock_savefig.assert_called_once_with("test_qq.png")
        
        with pytest.raises(ValueError):
            operators.qq_plot([], "test_qq.png")
    
    @patch('matplotlib.pyplot.savefig')
    def test_heatmap(self, mock_savefig, operators):
        """Test la heatmap."""
        assert operators.heatmap([[1, 2], [3, 4]], "test_heatmap.png") is True
        mock_savefig.assert_called_once_with("test_heatmap.png")
        
        with pytest.raises(ValueError):
            operators.heatmap([], "test_heatmap.png")
        with pytest.raises(ValueError):
            operators.heatmap([[1, 2], [3]], "test_heatmap.png")
    
    @patch('matplotlib.pyplot.savefig')
    def test_pie_chart(self, mock_savefig, operators):
        """Test le graphique en camembert."""
        assert operators.pie_chart([1, 2, 3], ["A", "B", "C"], "test_pie.png") is True
        mock_savefig.assert_called_once_with("test_pie.png")
        
        with pytest.raises(ValueError):
            operators.pie_chart([], ["A", "B", "C"], "test_pie.png")
        with pytest.raises(ValueError):
            operators.pie_chart([1, 2, 3], ["A", "B"], "test_pie.png")
    
    @patch('matplotlib.pyplot.savefig')
    def test_bar_chart(self, mock_savefig, operators):
        """Test le graphique en barres."""
        assert operators.bar_chart([1, 2, 3], ["A", "B", "C"], "test_bar.png") is True
        mock_savefig.assert_called_once_with("test_bar.png")
        
        with pytest.raises(ValueError):
            operators.bar_chart([], ["A", "B", "C"], "test_bar.png")
        with pytest.raises(ValueError):
            operators.bar_chart([1, 2, 3], ["A", "B"], "test_bar.png")
    
    def test_parse_list(self, operators):
        """Test l'analyse d'une liste."""
        assert operators.parse_list("1, 2, 3") == [1.0, 2.0, 3.0]
        
        with pytest.raises(ValueError):
            operators.parse_list("")
        with pytest.raises(ValueError):
            operators.parse_list("1, a, 3")
    
    def test_parse_two_lists(self, operators):
        """Test l'analyse de deux listes."""
        list1, list2 = operators.parse_two_lists("1, 2, 3; 4, 5, 6")
        assert list1 == [1.0, 2.0, 3.0]
        assert list2 == [4.0, 5.0, 6.0]
        
        with pytest.raises(ValueError):
            operators.parse_two_lists("")
        with pytest.raises(ValueError):
            operators.parse_two_lists("1, 2; 3")
        with pytest.raises(ValueError):
            operators.parse_two_lists("1, a; 3, 4")
    
    def test_parse_matrix(self, operators):
        """Test l'analyse d'une matrice."""
        assert operators.parse_matrix("1, 2; 3, 4") == [[1.0, 2.0], [3.0, 4.0]]
        
        with pytest.raises(ValueError):
            operators.parse_matrix("")
        with pytest.raises(ValueError):
            operators.parse_matrix("1, 2; 3")
        with pytest.raises(ValueError):
            operators.parse_matrix("1, a; 3, 4")
    
    def test_parse_pie_data(self, operators):
        """Test l'analyse des données pour un graphique en camembert."""
        values, labels = operators.parse_pie_data("1, 2, 3; A, B, C")
        assert values == [1.0, 2.0, 3.0]
        assert labels == ["A", "B", "C"]
        
        with pytest.raises(ValueError):
            operators.parse_pie_data("")
        with pytest.raises(ValueError):
            operators.parse_pie_data("1, 2; A")
    
    def test_parse_bar_data(self, operators):
        """Test l'analyse des données pour un graphique en barres."""
        values, labels = operators.parse_bar_data("1, 2, 3; A, B, C")
        assert values == [1.0, 2.0, 3.0]
        assert labels == ["A", "B", "C"]
        
        with pytest.raises(ValueError):
            operators.parse_bar_data("")
        with pytest.raises(ValueError):
            operators.parse_bar_data("1, 2; A")
    
    def test_parse_percentile(self, operators):
        """Test l'analyse du percentile."""
        values, percentile = operators.parse_percentile("1, 2, 3, 4, 5; 50")
        assert values == [1.0, 2.0, 3.0, 4.0, 5.0]
        assert percentile == 50.0
        
        with pytest.raises(ValueError):
            operators.parse_percentile("")
        with pytest.raises(ValueError):
            operators.parse_percentile("1, 2; ")
        with pytest.raises(ValueError):
            operators.parse_percentile("1, 2; a") 