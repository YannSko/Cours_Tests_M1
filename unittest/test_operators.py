import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from calculate.operators import Operators

class TestOperators(unittest.TestCase):
    """Tests pour la classe Operators avec unittest."""

    def setUp(self):
        """Configuration initiale pour chaque test."""
        self.operators = Operators()

    def test_basic_operations(self):
        """Test les opérations mathématiques de base."""
        # Addition
        self.assertEqual(self.operators.addition(2, 3), 5)
        self.assertEqual(self.operators.addition(-1, 1), 0)
        self.assertEqual(self.operators.addition(2.5, 3.5), 6.0)
        
        # Soustraction
        self.assertEqual(self.operators.substraction(5, 3), 2)
        self.assertEqual(self.operators.substraction(1, 1), 0)
        self.assertEqual(self.operators.substraction(5.5, 2.5), 3.0)
        
        # Multiplication
        self.assertEqual(self.operators.multiplication(2, 3), 6)
        self.assertEqual(self.operators.multiplication(-2, 3), -6)
        self.assertEqual(self.operators.multiplication(2.5, 2), 5.0)
        
        # Division
        self.assertEqual(self.operators.division(6, 2), 3)
        self.assertEqual(self.operators.division(5, 2), 2.5)
        
        with self.assertRaises(ValueError):
            self.operators.division(5, 0)

    def test_advanced_operations(self):
        """Test les opérations mathématiques avancées."""
        # Puissance
        self.assertEqual(self.operators.power(2, 3), 8)
        self.assertEqual(self.operators.power(2, 0), 1)
        self.assertEqual(self.operators.power(2, -1), 0.5)
        
        # Racine carrée
        self.assertEqual(self.operators.square_root(16), 4)
        self.assertAlmostEqual(self.operators.square_root(2), 1.4142, places=4)
        
        with self.assertRaises(ValueError):
            self.operators.square_root(-1)
        
        # Logarithme
        self.assertEqual(self.operators.logarithm(1), 0)
        self.assertAlmostEqual(self.operators.logarithm(np.e), 1, places=10)
        
        with self.assertRaises(ValueError):
            self.operators.logarithm(0)
            
        with self.assertRaises(ValueError):
            self.operators.logarithm(-1)
            
        # Modulo
        self.assertEqual(self.operators.modulo(5, 2), 1)
        self.assertEqual(self.operators.modulo(10, 3), 1)
        
        with self.assertRaises(ValueError):
            self.operators.modulo(5, 0)

    def test_trigonometric_operations(self):
        """Test les fonctions trigonométriques."""
        # Sinus
        self.assertAlmostEqual(self.operators.sine(0), 0, places=10)
        self.assertAlmostEqual(self.operators.sine(np.pi/2), 1, places=10)
        
        # Cosinus
        self.assertAlmostEqual(self.operators.cosine(0), 1, places=10)
        self.assertAlmostEqual(self.operators.cosine(np.pi), -1, places=10)
        
        # Tangente
        self.assertAlmostEqual(self.operators.tangent(0), 0, places=10)
        self.assertAlmostEqual(self.operators.tangent(np.pi/4), 1, places=10)
        
        # Cas spéciaux pour la tangente
        with self.assertRaises(ValueError):
            self.operators.tangent(np.pi/2)

    def test_factorial_operation(self):
        """Test la fonction factorielle."""
        self.assertEqual(self.operators.factorial(5), 120)
        self.assertEqual(self.operators.factorial(0), 1)
        
        with self.assertRaises(ValueError):
            self.operators.factorial(-1)
            
        with self.assertRaises(ValueError):
            self.operators.factorial(3.5)

    def test_absolute_operation(self):
        """Test la fonction valeur absolue."""
        self.assertEqual(self.operators.absolute(-5), 5)
        self.assertEqual(self.operators.absolute(5), 5)
        self.assertEqual(self.operators.absolute(0), 0)
        self.assertEqual(self.operators.absolute(-3.14), 3.14)

    def test_exponential_operation(self):
        """Test la fonction exponentielle."""
        self.assertEqual(self.operators.exponential(0), 1)
        self.assertAlmostEqual(self.operators.exponential(1), np.e, places=10)
        self.assertAlmostEqual(self.operators.exponential(2), np.e**2, places=10)

    def test_statistical_operations(self):
        """Test les fonctions statistiques."""
        # Moyenne
        self.assertEqual(self.operators.mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(self.operators.mean([2.5, 3.5]), 3.0)
        
        with self.assertRaises(ValueError):
            self.operators.mean([])
        
        # Médiane
        self.assertEqual(self.operators.median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(self.operators.median([1, 2, 3, 4]), 2.5)
        
        with self.assertRaises(ValueError):
            self.operators.median([])
        
        # Mode
        self.assertEqual(self.operators.mode([1, 2, 2, 3, 3, 3]), 3)
        self.assertIn(self.operators.mode([1, 1, 2, 2]), [1, 2])  # Plusieurs modes possibles
        
        with self.assertRaises(ValueError):
            self.operators.mode([])
        
        # Écart-type
        self.assertAlmostEqual(self.operators.standard_deviation([1, 2, 3, 4, 5]), 1.4142, places=4)
        self.assertEqual(self.operators.standard_deviation([0, 0, 0]), 0)
        
        with self.assertRaises(ValueError):
            self.operators.standard_deviation([])
        
        # Variance
        self.assertEqual(self.operators.variance([1, 2, 3, 4, 5]), 2)
        self.assertEqual(self.operators.variance([0, 0, 0]), 0)
        
        with self.assertRaises(ValueError):
            self.operators.variance([])

    def test_advanced_statistical_operations(self):
        """Test les fonctions statistiques avancées."""
        # Percentile
        self.assertEqual(self.operators.percentile([1, 2, 3, 4, 5], 50), 3)
        self.assertEqual(self.operators.percentile([1, 2, 3, 4, 5], 75), 4)
        
        with self.assertRaises(ValueError):
            self.operators.percentile([], 50)
            
        with self.assertRaises(ValueError):
            self.operators.percentile([1, 2, 3], -10)
            
        with self.assertRaises(ValueError):
            self.operators.percentile([1, 2, 3], 110)
        
        # Corrélation
        self.assertEqual(self.operators.correlation([1, 2, 3], [4, 5, 6]), 1)
        self.assertEqual(self.operators.correlation([1, 2, 3], [6, 5, 4]), -1)
        
        with self.assertRaises(ValueError):
            self.operators.correlation([], [1, 2])
            
        with self.assertRaises(ValueError):
            self.operators.correlation([1, 2], [1])
        
        # Régression linéaire
        slope, intercept = self.operators.regression([1, 2, 3], [4, 5, 6])
        self.assertEqual(slope, 1)
        self.assertEqual(intercept, 3)
        
        with self.assertRaises(ValueError):
            self.operators.regression([], [1, 2])
            
        with self.assertRaises(ValueError):
            self.operators.regression([1, 2], [1])

    @patch('matplotlib.pyplot.savefig')
    def test_visualization_functions(self, mock_savefig):
        """Test les fonctions de visualisation."""
        # Configuration du mock pour simuler la sauvegarde du graphique
        mock_savefig.return_value = None
        
        # Plot
        self.assertTrue(self.operators.plot("x**2", -10, 10, "test_plot.png"))
        mock_savefig.assert_called_once_with("test_plot.png")
        mock_savefig.reset_mock()
        
        # Plot avec erreur
        with self.assertRaises(ValueError):
            self.operators.plot("syntax error", -10, 10, "test_plot.png")
        
        # Scatter
        self.assertTrue(self.operators.scatter([1, 2, 3], [4, 5, 6], "test_scatter.png"))
        mock_savefig.assert_called_once_with("test_scatter.png")
        mock_savefig.reset_mock()
        
        # Scatter avec erreur
        with self.assertRaises(ValueError):
            self.operators.scatter([], [4, 5, 6], "test_scatter.png")
            
        with self.assertRaises(ValueError):
            self.operators.scatter([1, 2, 3], [4, 5], "test_scatter.png")
        
        # Histogram
        self.assertTrue(self.operators.histogram([1, 2, 2, 3, 3, 3, 4, 4, 5], "test_histogram.png"))
        mock_savefig.assert_called_once_with("test_histogram.png")
        mock_savefig.reset_mock()
        
        # Histogram avec erreur
        with self.assertRaises(ValueError):
            self.operators.histogram([], "test_histogram.png")

    def test_validate_numeric_input(self):
        """Test la validation des entrées numériques."""
        # Cas valides
        self.assertTrue(self.operators._validate_numeric_input(5))
        self.assertTrue(self.operators._validate_numeric_input(3.14))
        self.assertTrue(self.operators._validate_numeric_input(-10))
        
        # Cas invalides
        with self.assertRaises(ValueError):
            self.operators._validate_numeric_input("abc")
            
        with self.assertRaises(ValueError):
            self.operators._validate_numeric_input(None)

    def test_validate_list_input(self):
        """Test la validation des entrées de liste."""
        # Cas valides
        self.assertTrue(self.operators._validate_list_input([1, 2, 3]))
        self.assertTrue(self.operators._validate_list_input([1.5, 2.5, 3.5]))
        
        # Cas invalides
        with self.assertRaises(ValueError):
            self.operators._validate_list_input([])
            
        with self.assertRaises(ValueError):
            self.operators._validate_list_input([1, "abc", 3])
            
        with self.assertRaises(ValueError):
            self.operators._validate_list_input(None)
            
        with self.assertRaises(ValueError):
            self.operators._validate_list_input("abc")

    def test_validate_matrix_input(self):
        """Test la validation des entrées de matrice."""
        # Cas valides
        self.assertTrue(self.operators._validate_matrix_input([[1, 2], [3, 4]]))
        self.assertTrue(self.operators._validate_matrix_input([[1.5], [2.5]]))
        
        # Cas invalides
        with self.assertRaises(ValueError):
            self.operators._validate_matrix_input([])
            
        with self.assertRaises(ValueError):
            self.operators._validate_matrix_input([[1, 2], [3]])
            
        with self.assertRaises(ValueError):
            self.operators._validate_matrix_input([[1, "abc"], [3, 4]])
            
        with self.assertRaises(ValueError):
            self.operators._validate_matrix_input(None)
            
        with self.assertRaises(ValueError):
            self.operators._validate_matrix_input("abc")


if __name__ == '__main__':
    unittest.main() 