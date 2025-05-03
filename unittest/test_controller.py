import unittest
from unittest.mock import patch, MagicMock, call
from calculate.controller import Controller
from calculate.view import View
from calculate.operators import Operators

class TestController(unittest.TestCase):
    """Tests pour la classe Controller avec unittest."""

    def setUp(self):
        """Configuration initiale pour chaque test."""
        self.mock_view = MagicMock(spec=View)
        self.mock_operators = MagicMock(spec=Operators)
        self.controller = Controller(self.mock_view, self.mock_operators)

    def test_init(self):
        """Test l'initialisation du contrôleur."""
        self.assertEqual(self.controller.view, self.mock_view)
        self.assertEqual(self.controller.operators, self.mock_operators)

    def test_init_error(self):
        """Test la gestion d'erreur pendant l'initialisation."""
        with self.assertRaises(ValueError):
            Controller(None, self.mock_operators)
            
        with self.assertRaises(ValueError):
            Controller(self.mock_view, None)

    def test_is_input_valid(self):
        """Test la validation de l'entrée utilisateur."""
        # Entrées valides
        self.assertTrue(self.controller._is_input_valid("2 + 3"))
        self.assertTrue(self.controller._is_input_valid("sqrt(16)"))
        self.assertTrue(self.controller._is_input_valid("mean(1,2,3,4,5)"))
        self.assertTrue(self.controller._is_input_valid("help"))
        self.assertTrue(self.controller._is_input_valid("exit"))
        
        # Entrées invalides
        self.assertFalse(self.controller._is_input_valid(""))
        self.assertFalse(self.controller._is_input_valid("   "))
        self.assertFalse(self.controller._is_input_valid("invalid command"))

    def test_is_quit(self):
        """Test la condition de sortie."""
        # Commandes de sortie
        self.assertTrue(self.controller._is_quit("exit"))
        self.assertTrue(self.controller._is_quit("quit"))
        self.assertTrue(self.controller._is_quit("q"))
        
        # Commandes qui ne sont pas des sorties
        self.assertFalse(self.controller._is_quit("help"))
        self.assertFalse(self.controller._is_quit("2 + 3"))
        self.assertFalse(self.controller._is_quit(""))

    def test_is_quit_error(self):
        """Test la gestion d'erreur de la condition de sortie."""
        # Cas d'erreur avec une entrée None
        self.assertFalse(self.controller._is_quit(None))

    def test_operations_basic(self):
        """Test les opérations de base."""
        # Préparation des mocks
        self.mock_operators.addition.return_value = 5
        self.mock_operators.substraction.return_value = 2
        self.mock_operators.multiplication.return_value = 6
        self.mock_operators.division.return_value = 3
        
        # Addition
        result = self.controller._operations("2 + 3")
        self.assertEqual(result, 5)
        self.mock_operators.addition.assert_called_once_with(2, 3)
        
        # Soustraction
        result = self.controller._operations("5 - 3")
        self.assertEqual(result, 2)
        self.mock_operators.substraction.assert_called_once_with(5, 3)
        
        # Multiplication
        result = self.controller._operations("2 * 3")
        self.assertEqual(result, 6)
        self.mock_operators.multiplication.assert_called_once_with(2, 3)
        
        # Division
        result = self.controller._operations("6 / 2")
        self.assertEqual(result, 3)
        self.mock_operators.division.assert_called_once_with(6, 2)

    def test_operations_advanced(self):
        """Test les opérations avancées."""
        # Préparation des mocks
        self.mock_operators.square_root.return_value = 4
        self.mock_operators.power.return_value = 8
        self.mock_operators.logarithm.return_value = 0
        self.mock_operators.modulo.return_value = 1
        self.mock_operators.sine.return_value = 0
        self.mock_operators.cosine.return_value = 1
        self.mock_operators.tangent.return_value = 0
        self.mock_operators.factorial.return_value = 120
        self.mock_operators.absolute.return_value = 5
        self.mock_operators.exponential.return_value = 1
        
        # Racine carrée
        result = self.controller._operations("sqrt(16)")
        self.assertEqual(result, 4)
        self.mock_operators.square_root.assert_called_once_with(16)
        
        # Puissance
        result = self.controller._operations("2 ^ 3")
        self.assertEqual(result, 8)
        self.mock_operators.power.assert_called_once_with(2, 3)
        
        # Logarithme
        result = self.controller._operations("log(1)")
        self.assertEqual(result, 0)
        self.mock_operators.logarithm.assert_called_once_with(1)
        
        # Modulo
        result = self.controller._operations("5 % 2")
        self.assertEqual(result, 1)
        self.mock_operators.modulo.assert_called_once_with(5, 2)
        
        # Sinus
        result = self.controller._operations("sin(0)")
        self.assertEqual(result, 0)
        self.mock_operators.sine.assert_called_once_with(0)
        
        # Cosinus
        result = self.controller._operations("cos(0)")
        self.assertEqual(result, 1)
        self.mock_operators.cosine.assert_called_once_with(0)
        
        # Tangente
        result = self.controller._operations("tan(0)")
        self.assertEqual(result, 0)
        self.mock_operators.tangent.assert_called_once_with(0)
        
        # Factorielle
        result = self.controller._operations("5!")
        self.assertEqual(result, 120)
        self.mock_operators.factorial.assert_called_once_with(5)
        
        # Valeur absolue
        result = self.controller._operations("abs(-5)")
        self.assertEqual(result, 5)
        self.mock_operators.absolute.assert_called_once_with(-5)
        
        # Exponentielle
        result = self.controller._operations("exp(0)")
        self.assertEqual(result, 1)
        self.mock_operators.exponential.assert_called_once_with(0)

    def test_operations_statistics(self):
        """Test les opérations statistiques."""
        # Préparation des mocks
        self.mock_operators.mean.return_value = 3
        self.mock_operators.median.return_value = 3
        self.mock_operators.mode.return_value = 3
        self.mock_operators.standard_deviation.return_value = 1.414
        self.mock_operators.variance.return_value = 2
        self.mock_operators.percentile.return_value = 3
        self.mock_operators.correlation.return_value = 1
        self.mock_operators.linear_regression.return_value = (1, 3)
        
        # Moyenne
        result = self.controller._operations("mean(1,2,3,4,5)")
        self.assertEqual(result, 3)
        self.mock_operators.mean.assert_called_once_with([1, 2, 3, 4, 5])
        
        # Médiane
        result = self.controller._operations("median(1,2,3,4,5)")
        self.assertEqual(result, 3)
        self.mock_operators.median.assert_called_once_with([1, 2, 3, 4, 5])
        
        # Mode
        result = self.controller._operations("mode(1,2,3,3,3)")
        self.assertEqual(result, 3)
        self.mock_operators.mode.assert_called_once_with([1, 2, 3, 3, 3])
        
        # Écart-type
        result = self.controller._operations("std(1,2,3,4,5)")
        self.assertEqual(result, 1.414)
        self.mock_operators.standard_deviation.assert_called_once_with([1, 2, 3, 4, 5])
        
        # Variance
        result = self.controller._operations("var(1,2,3,4,5)")
        self.assertEqual(result, 2)
        self.mock_operators.variance.assert_called_once_with([1, 2, 3, 4, 5])
        
        # Percentile
        result = self.controller._operations("percentile(1,2,3,4,5;50)")
        self.assertEqual(result, 3)
        self.mock_operators.percentile.assert_called_once_with([1, 2, 3, 4, 5], 50)
        
        # Corrélation
        result = self.controller._operations("correlation(1,2,3;4,5,6)")
        self.assertEqual(result, 1)
        self.mock_operators.correlation.assert_called_once_with([1, 2, 3], [4, 5, 6])
        
        # Régression linéaire
        result = self.controller._operations("regression(1,2,3;4,5,6)")
        self.assertEqual(result, (1, 3))
        self.mock_operators.linear_regression.assert_called_once_with([1, 2, 3], [4, 5, 6])

    def test_operations_visualization(self):
        """Test les opérations de visualisation."""
        # Préparation des mocks
        self.mock_operators.plot.return_value = True
        self.mock_operators.scatter.return_value = True
        self.mock_operators.histogram.return_value = True
        self.mock_operators.polar.return_value = True
        self.mock_operators.plot_3d.return_value = True
        self.mock_operators.boxplot.return_value = True
        self.mock_operators.qq_plot.return_value = True
        self.mock_operators.heatmap.return_value = True
        self.mock_operators.pie_chart.return_value = True
        self.mock_operators.bar_chart.return_value = True
        
        # Plot
        result = self.controller._operations("plot(x**2,-10,10,graph.png)")
        self.assertTrue(result)
        self.mock_operators.plot.assert_called_once_with("x**2", -10, 10, "graph.png")
        
        # Scatter
        result = self.controller._operations("scatter(1,2,3;4,5,6;scatter.png)")
        self.assertTrue(result)
        self.mock_operators.scatter.assert_called_once_with([1, 2, 3], [4, 5, 6], "scatter.png")
        
        # Histogram
        result = self.controller._operations("histogram(1,2,2,3,3,3;hist.png)")
        self.assertTrue(result)
        self.mock_operators.histogram.assert_called_once_with([1, 2, 2, 3, 3, 3], "hist.png")
        
        # Polar
        result = self.controller._operations("polar(0,1.57,3.14;1,2,3;polar.png)")
        self.assertTrue(result)
        self.mock_operators.polar.assert_called_once_with([0, 1.57, 3.14], [1, 2, 3], "polar.png")
        
        # 3D
        result = self.controller._operations("3d(1,2;3,4;5,6;3d.png)")
        self.assertTrue(result)
        self.mock_operators.plot_3d.assert_called_once_with([1, 2], [3, 4], [5, 6], "3d.png")
        
        # Boxplot
        result = self.controller._operations("boxplot(1,2,3,4,5;boxplot.png)")
        self.assertTrue(result)
        self.mock_operators.boxplot.assert_called_once_with([1, 2, 3, 4, 5], "boxplot.png")
        
        # QQ plot
        result = self.controller._operations("qq(1,2,3,4,5;qq.png)")
        self.assertTrue(result)
        self.mock_operators.qq_plot.assert_called_once_with([1, 2, 3, 4, 5], "qq.png")
        
        # Heatmap
        result = self.controller._operations("heatmap(1,2;3,4;heatmap.png)")
        self.assertTrue(result)
        self.mock_operators.heatmap.assert_called_once_with([[1, 2], [3, 4]], "heatmap.png")
        
        # Pie chart
        result = self.controller._operations("pie(1,2,3;A,B,C;pie.png)")
        self.assertTrue(result)
        self.mock_operators.pie_chart.assert_called_once_with([1, 2, 3], ["A", "B", "C"], "pie.png")
        
        # Bar chart
        result = self.controller._operations("bar(1,2,3;A,B,C;bar.png)")
        self.assertTrue(result)
        self.mock_operators.bar_chart.assert_called_once_with([1, 2, 3], ["A", "B", "C"], "bar.png")

    def test_operations_error_handling(self):
        """Test la gestion des erreurs dans les opérations."""
        # Préparation du mock pour lever une exception
        self.mock_operators.division.side_effect = ValueError("Division par zéro")
        
        # Test avec une opération qui lève une exception
        result = self.controller._operations("5 / 0")
        self.assertIsNone(result)
        self.mock_view.print_error.assert_called_once_with("Division par zéro")
        
        # Test avec une opération invalide
        result = self.controller._operations("invalid operation")
        self.assertIsNone(result)
        self.mock_view.print_error.assert_called_with("Opération non prise en charge: invalid operation")

    def test_run_cycle(self):
        """Test le cycle d'exécution complet."""
        # Préparation des mocks
        self.mock_view.get_user_input.side_effect = ["2 + 3", "exit"]
        self.mock_operators.addition.return_value = 5
        
        # Exécution de la méthode run
        self.controller.run()
        
        # Vérification des appels
        self.mock_view.print_welcome.assert_called_once()
        self.mock_view.print_menu.assert_called()
        self.mock_view.get_user_input.assert_called_with("Entrez une opération (ou 'help', 'exit'): ")
        self.mock_operators.addition.assert_called_once_with(2, 3)
        self.mock_view.print_result.assert_called_once_with("2 + 3", 5)
        self.mock_view.continue_message.assert_called_once()
        self.mock_view.end_message.assert_called_once()

    def test_run_help_command(self):
        """Test la commande d'aide."""
        # Préparation des mocks
        self.mock_view.get_user_input.side_effect = ["help", "help stats", "help visualization", "exit"]
        
        # Exécution de la méthode run
        self.controller.run()
        
        # Vérification des appels
        self.mock_view.print_welcome.assert_called_once()
        self.mock_view.print_help.assert_called_once()
        self.mock_view.print_statistics_help.assert_called_once()
        self.mock_view.print_visualization_help.assert_called_once()
        self.mock_view.end_message.assert_called_once()

    def test_run_error_handling(self):
        """Test la gestion des erreurs pendant l'exécution."""
        # Préparation des mocks pour simuler une erreur
        self.mock_view.get_user_input.side_effect = Exception("Erreur simulée")
        
        # Exécution de la méthode run
        self.controller.run()
        
        # Vérification des appels
        self.mock_view.print_welcome.assert_called_once()
        self.mock_view.print_error.assert_called_with("Erreur lors de l'exécution: Erreur simulée")
        self.mock_view.end_message.assert_called_once()

    def test_run_invalid_input(self):
        """Test avec une entrée invalide."""
        # Préparation des mocks
        self.mock_view.get_user_input.side_effect = ["invalid command", "exit"]
        
        # Exécution de la méthode run
        self.controller.run()
        
        # Vérification des appels
        self.mock_view.print_welcome.assert_called_once()
        self.mock_view.print_error.assert_called_with("Entrée invalide")
        self.mock_view.end_message.assert_called_once()

    def test_run_empty_input(self):
        """Test avec une entrée vide."""
        # Préparation des mocks
        self.mock_view.get_user_input.side_effect = ["", "exit"]
        
        # Exécution de la méthode run
        self.controller.run()
        
        # Vérification des appels
        self.mock_view.print_welcome.assert_called_once()
        self.mock_view.print_error.assert_called_with("Entrée invalide")
        self.mock_view.end_message.assert_called_once()
        
    def test_run_consecutive_operations(self):
        """Test plusieurs opérations consécutives."""
        # Préparation des mocks
        self.mock_view.get_user_input.side_effect = ["2 + 3", "5 - 2", "exit"]
        self.mock_operators.addition.return_value = 5
        self.mock_operators.substraction.return_value = 3
        
        # Exécution de la méthode run
        self.controller.run()
        
        # Vérification des appels
        self.mock_operators.addition.assert_called_once_with(2, 3)
        self.mock_operators.substraction.assert_called_once_with(5, 2)
        self.mock_view.print_result.assert_any_call("2 + 3", 5)
        self.mock_view.print_result.assert_any_call("5 - 2", 3)
        self.mock_view.continue_message.assert_called()
        self.mock_view.end_message.assert_called_once()
    
    def test_operations_parsing(self):
        """Test l'analyse des chaînes d'opération."""
        # Addition
        self.controller._operations("2 + 3")
        self.mock_operators.addition.assert_called_once_with("2 + 3")
        
        # Soustraction
        self.controller._operations("5 - 3")
        self.mock_operators.substraction.assert_called_once_with("5 - 3")
        
        # Opération invalide
        result = self.controller._operations("invalid")
        self.assertIsNone(result)
        self.mock_view.print_error.assert_called_with("Opération non prise en charge: invalid")
    
    def test_is_help_command(self):
        """Test la détection des commandes d'aide."""
        # Commandes d'aide
        self.assertTrue(self.controller._is_help_command("help"))
        self.assertTrue(self.controller._is_help_command("help stats"))
        self.assertTrue(self.controller._is_help_command("help visualization"))
        
        # Commandes qui ne sont pas de l'aide
        self.assertFalse(self.controller._is_help_command("exit"))
        self.assertFalse(self.controller._is_help_command("2 + 3"))
        self.assertFalse(self.controller._is_help_command(""))
    
    def test_handle_help_command(self):
        """Test la gestion des commandes d'aide."""
        # Aide générale
        self.controller._handle_help_command("help")
        self.mock_view.print_help.assert_called_once()
        
        # Aide statistique
        self.controller._handle_help_command("help stats")
        self.mock_view.print_statistics_help.assert_called_once()
        
        # Aide visualisation
        self.controller._handle_help_command("help visualization")
        self.mock_view.print_visualization_help.assert_called_once()
        
        # Aide non reconnue
        self.controller._handle_help_command("help unknown")
        self.mock_view.print_error.assert_called_with("Commande d'aide non reconnue: unknown")


if __name__ == '__main__':
    unittest.main() 