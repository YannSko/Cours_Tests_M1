import unittest
from unittest.mock import patch, MagicMock, call
from calculate.controller import Controller
from calculate.view import View
from calculate.operators import Operators

class TestController(unittest.TestCase):
    """Tests pour la classe Controller avec unittest."""

    def setUp(self):
        """Configuration initiale pour chaque test."""
        self.controller = Controller()
        # Mock les dépendances
        self.controller.operator = MagicMock(spec=Operators)
        
        # Patch statique pour View
        self.view_patcher = patch('calculate.controller.View')
        self.mock_view = self.view_patcher.start()
        
    def tearDown(self):
        """Nettoyage après chaque test."""
        self.view_patcher.stop()

    def test_init(self):
        """Test l'initialisation du contrôleur."""
        controller = Controller()
        self.assertIsInstance(controller.operator, Operators)
        self.assertIsNone(controller.result)

    def test_is_input_valid(self):
        """Test la validation de l'entrée utilisateur."""
        # Entrées valides
        for i in range(1, 35):
            self.assertTrue(self.controller._is_input_valid(str(i)))
        self.assertTrue(self.controller._is_input_valid("help"))
        
        # Entrées invalides
        self.assertFalse(self.controller._is_input_valid(""))
        self.assertFalse(self.controller._is_input_valid("   "))
        self.assertFalse(self.controller._is_input_valid("invalid command"))
        self.assertFalse(self.controller._is_input_valid("exit"))

    def test_is_quit(self):
        """Test la condition de sortie."""
        # Si l'entrée est "34", _is_quit devrait retourner False (pour terminer la boucle)
        self.assertFalse(self.controller._is_quit("34"))
        
        # Pour toutes les autres entrées, _is_quit devrait retourner True
        self.assertTrue(self.controller._is_quit("1"))
        self.assertTrue(self.controller._is_quit("help"))
        self.assertTrue(self.controller._is_quit("exit"))
        self.assertTrue(self.controller._is_quit(""))

    def test_operations_basic(self):
        """Test les opérations de base."""
        # Configuration des mocks
        self.controller.operator.addition.return_value = 5
        self.controller.operator.substraction.return_value = 2
        self.controller.operator.multiplication.return_value = 6
        self.controller.operator.division.return_value = 3
        self.mock_view.get_user_input.return_value = "test_operation"
        
        # Addition
        self.controller._operations("1")
        self.assertEqual(self.controller.result, 5)
        self.controller.operator.addition.assert_called_once_with("test_operation")
        
        # Soustraction
        self.controller._operations("2")
        self.assertEqual(self.controller.result, 2)
        self.controller.operator.substraction.assert_called_once_with("test_operation")
        
        # Multiplication
        self.controller._operations("3")
        self.assertEqual(self.controller.result, 6)
        self.controller.operator.multiplication.assert_called_once_with("test_operation")
        
        # Division
        self.controller._operations("4")
        self.assertEqual(self.controller.result, 3)
        self.controller.operator.division.assert_called_once_with("test_operation")

    def test_operations_advanced(self):
        """Test les opérations avancées."""
        # Configuration des mocks
        self.controller.operator.power.return_value = 8
        self.controller.operator.square_root.return_value = 4
        self.controller.operator.logarithm.return_value = 0
        self.controller.operator.modulo.return_value = 1
        self.controller.operator.sine.return_value = 0
        self.controller.operator.cosine.return_value = 1
        self.controller.operator.tangent.return_value = 0
        self.controller.operator.factorial.return_value = 120
        self.controller.operator.absolute.return_value = 5
        self.controller.operator.exponential.return_value = 1
        self.mock_view.get_user_input.return_value = "test_operation"
        
        # Puissance
        self.controller._operations("5")
        self.assertEqual(self.controller.result, 8)
        self.controller.operator.power.assert_called_once_with("test_operation")
        
        # Racine carrée
        self.controller._operations("6")
        self.assertEqual(self.controller.result, 4)
        self.controller.operator.square_root.assert_called_once_with("test_operation")
        
        # Logarithme
        self.controller._operations("7")
        self.assertEqual(self.controller.result, 0)
        self.controller.operator.logarithm.assert_called_once_with("test_operation")
        
        # Modulo
        self.controller._operations("8")
        self.assertEqual(self.controller.result, 1)
        self.controller.operator.modulo.assert_called_once_with("test_operation")
        
        # Sinus
        self.controller._operations("9")
        self.assertEqual(self.controller.result, 0)
        self.controller.operator.sine.assert_called_once_with("test_operation")
        
        # Cosinus
        self.controller._operations("10")
        self.assertEqual(self.controller.result, 1)
        self.controller.operator.cosine.assert_called_once_with("test_operation")
        
        # Tangente
        self.controller._operations("11")
        self.assertEqual(self.controller.result, 0)
        self.controller.operator.tangent.assert_called_once_with("test_operation")
        
        # Factorielle
        self.controller._operations("12")
        self.assertEqual(self.controller.result, 120)
        self.controller.operator.factorial.assert_called_once_with("test_operation")
        
        # Valeur absolue
        self.controller._operations("13")
        self.assertEqual(self.controller.result, 5)
        self.controller.operator.absolute.assert_called_once_with("test_operation")
        
        # Exponentielle
        self.controller._operations("14")
        self.assertEqual(self.controller.result, 1)
        self.controller.operator.exponential.assert_called_once_with("test_operation")

    def test_operations_statistics(self):
        """Test les opérations statistiques."""
        # Configuration des mocks
        self.controller.operator.mean.return_value = 3
        self.controller.operator.median.return_value = 3
        self.controller.operator.mode.return_value = 3
        self.controller.operator.standard_deviation.return_value = 1.414
        self.controller.operator.variance.return_value = 2
        self.controller.operator.percentile.return_value = 3
        self.controller.operator.correlation.return_value = 1
        self.controller.operator.linear_regression.return_value = (1, 3)
        self.mock_view.get_user_input.return_value = "test_operation"
        
        # Moyenne
        self.controller._operations("15")
        self.assertEqual(self.controller.result, 3)
        self.controller.operator.mean.assert_called_once_with("test_operation")
        
        # Médiane
        self.controller._operations("16")
        self.assertEqual(self.controller.result, 3)
        self.controller.operator.median.assert_called_once_with("test_operation")
        
        # Mode
        self.controller._operations("17")
        self.assertEqual(self.controller.result, 3)
        self.controller.operator.mode.assert_called_once_with("test_operation")
        
        # Écart-type
        self.controller._operations("18")
        self.assertEqual(self.controller.result, 1.414)
        self.controller.operator.standard_deviation.assert_called_once_with("test_operation")
        
        # Variance
        self.controller._operations("19")
        self.assertEqual(self.controller.result, 2)
        self.controller.operator.variance.assert_called_once_with("test_operation")
        
        # Percentile
        self.controller._operations("20")
        self.assertEqual(self.controller.result, 3)
        self.controller.operator.percentile.assert_called_once_with("test_operation")
        
        # Corrélation
        self.controller._operations("21")
        self.assertEqual(self.controller.result, 1)
        self.controller.operator.correlation.assert_called_once_with("test_operation")
        
        # Régression linéaire
        self.controller._operations("22")
        self.assertEqual(self.controller.result, (1, 3))
        self.controller.operator.linear_regression.assert_called_once_with("test_operation")

    def test_operations_visualization(self):
        """Test les opérations de visualisation."""
        # Configuration des mocks
        self.controller.operator.visualize.return_value = True
        self.mock_view.get_user_input.return_value = "test_operation"
        
        # Tests de visualisation
        for i in range(23, 33):
            self.controller._operations(str(i))
            self.assertEqual(self.controller.result, True)
        
        # Vérifier que visualize a été appelé le bon nombre de fois
        self.assertEqual(self.controller.operator.visualize.call_count, 10)
        # Vérifier que tous les appels ont utilisé "test_operation"
        expected_calls = [call("test_operation") for _ in range(10)]
        self.controller.operator.visualize.assert_has_calls(expected_calls)

    def test_operations_error_handling(self):
        """Test la gestion des erreurs dans les opérations."""
        # Configuration des mocks
        self.mock_view.get_user_input.return_value = "invalid_operation"
        self.controller.operator.addition.side_effect = ValueError("Division par zéro")
        
        # Rediriger stdout pour capturer l'erreur
        with patch('builtins.print') as mock_print:
            # Test d'une opération qui lève une exception ValueError
            self.controller._operations("1")
            mock_print.assert_called_with("\nErreur: Division par zéro")
        
        # Test d'une exception générique
        self.controller.operator.addition.side_effect = Exception("Erreur générique")
        with patch('builtins.print') as mock_print:
            self.controller._operations("1")
            mock_print.assert_called_with("\nUne erreur inattendue s'est produite: Erreur générique")

    def test_run_basic_cycle(self):
        """Test le cycle d'exécution complet."""
        # Configuration des mocks
        self.mock_view.get_user_input.side_effect = ["1", "2+3", "34"]
        self.controller.operator.addition.return_value = 5
        
        # Exécution de la méthode run
        self.controller.run()
        
        # Vérification des appels
        self.mock_view.print_menu.assert_called()
        self.mock_view.get_user_input.assert_called()
        self.controller.operator.addition.assert_called_once_with("2+3")
        self.mock_view.print_result.assert_called_once_with("2+3", 5)
        self.mock_view.continue_message.assert_called_once()
        self.mock_view.end_message.assert_called_once()

    def test_run_help_command(self):
        """Test la commande d'aide."""
        # Configuration des mocks
        self.mock_view.get_user_input.side_effect = ["help", "34"]
        
        # Exécution de la méthode run
        self.controller.run()
        
        # Vérification des appels
        self.mock_view.print_menu.assert_called()
        self.mock_view.print_visualization_help.assert_called_once()
        self.mock_view.end_message.assert_called_once()

    def test_run_invalid_input(self):
        """Test avec une entrée invalide."""
        # Configuration des mocks
        self.mock_view.get_user_input.side_effect = ["invalid", "34"]
        
        # Exécution de la méthode run
        self.controller.run()
        
        # Vérification que le menu est affiché mais aucune opération n'est exécutée
        self.mock_view.print_menu.assert_called()
        self.mock_view.get_user_input.assert_called()
        self.mock_view.end_message.assert_called_once()

    def test_run_multiple_operations(self):
        """Test plusieurs opérations consécutives."""
        # Configuration des mocks
        self.mock_view.get_user_input.side_effect = ["1", "2+3", "2", "5-2", "34"]
        self.controller.operator.addition.return_value = 5
        self.controller.operator.substraction.return_value = 3
        
        # Exécution de la méthode run
        self.controller.run()
        
        # Vérification des appels
        self.controller.operator.addition.assert_called_once_with("2+3")
        self.controller.operator.substraction.assert_called_once_with("5-2")
        self.assertEqual(self.mock_view.print_result.call_count, 2)
        self.assertEqual(self.mock_view.continue_message.call_count, 2)
        self.mock_view.end_message.assert_called_once()


if __name__ == '__main__':
    unittest.main() 