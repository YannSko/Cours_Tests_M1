import pytest
from unittest.mock import patch, MagicMock
from calculate.controller import Controller
from calculate.view import View
from calculate.operators import Operators

class TestController:
    """Tests pour le module Controller."""

    @pytest.fixture
    def controller(self):
        """Fixture pour créer une instance de Controller."""
        return Controller()

    @patch('calculate.view.View.print_menu')
    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    @patch('calculate.view.View.end_message')
    def test_run_basic_operations(self, mock_end, mock_continue, mock_print_result, 
                                mock_get_input, mock_print_menu, controller):
        """Test du cycle complet d'exécution avec les opérations de base."""
        # Configuration des mocks
        mock_get_input.side_effect = ["1", "2 + 3", "34"]  # Addition, opération, quitter
        mock_print_result.return_value = None
        mock_continue.return_value = None

        # Exécution
        controller.run()

        # Vérifications
        assert mock_print_menu.call_count == 2  # Appelé au début et après l'opération
        assert mock_get_input.call_count == 3
        mock_print_result.assert_called_once()
        mock_continue.assert_called_once()
        mock_end.assert_called_once()

    @patch('calculate.view.View.print_menu')
    @patch('calculate.view.View.get_user_input')
    def test_run_invalid_input(self, mock_get_input, mock_print_menu, controller):
        """Test avec une entrée invalide."""
        mock_get_input.side_effect = ["invalid", "34"]
        controller.run()
        assert mock_print_menu.call_count == 2

    def test_is_input_valid(self, controller):
        """Test de la validation des entrées."""
        # Test des entrées valides
        assert controller._is_input_valid("1")  # Addition
        assert controller._is_input_valid("2")  # Soustraction
        assert controller._is_input_valid("3")  # Multiplication
        assert controller._is_input_valid("4")  # Division
        assert controller._is_input_valid("help")  # Aide

        # Test des entrées invalides
        assert not controller._is_input_valid("0")
        assert not controller._is_input_valid("35")
        assert not controller._is_input_valid("a")
        assert not controller._is_input_valid("")

    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    def test_operations_addition(self, mock_continue, mock_print_result, 
                               mock_get_input, controller):
        """Test de l'opération d'addition."""
        mock_get_input.return_value = "2 + 3"
        controller._operations("1")
        mock_print_result.assert_called_once_with("2 + 3", 5)
        mock_continue.assert_called_once()

    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    def test_operations_subtraction(self, mock_continue, mock_print_result, 
                                  mock_get_input, controller):
        """Test de l'opération de soustraction."""
        mock_get_input.return_value = "5 - 3"
        controller._operations("2")
        mock_print_result.assert_called_once_with("5 - 3", 2)
        mock_continue.assert_called_once()

    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    def test_operations_multiplication(self, mock_continue, mock_print_result, 
                                     mock_get_input, controller):
        """Test de l'opération de multiplication."""
        mock_get_input.return_value = "2 * 3"
        controller._operations("3")
        mock_print_result.assert_called_once_with("2 * 3", 6)
        mock_continue.assert_called_once()

    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    def test_operations_division(self, mock_continue, mock_print_result, 
                               mock_get_input, controller):
        """Test de l'opération de division."""
        mock_get_input.return_value = "6 / 2"
        controller._operations("4")
        mock_print_result.assert_called_once_with("6 / 2", 3)
        mock_continue.assert_called_once()

    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    def test_operations_division_by_zero(self, mock_continue, mock_print_result, 
                                       mock_get_input, controller):
        """Test de la division par zéro."""
        mock_get_input.return_value = "5 / 0"
        with pytest.raises(ValueError):
            controller._operations("4")

    def test_is_quit(self, controller):
        """Test de la condition de sortie."""
        assert controller._is_quit("1")  # Ne devrait pas quitter
        assert controller._is_quit("2")  # Ne devrait pas quitter
        assert controller._is_quit("3")  # Ne devrait pas quitter
        assert controller._is_quit("4")  # Ne devrait pas quitter
        assert not controller._is_quit("34")  # Devrait quitter

    @patch('calculate.view.View.print_menu')
    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    @patch('calculate.view.View.end_message')
    def test_run_multiple_operations(self, mock_end, mock_continue, mock_print_result, 
                                   mock_get_input, mock_print_menu, controller):
        """Test de plusieurs opérations consécutives."""
        mock_get_input.side_effect = ["1", "2 + 3", "2", "5 - 3", "34"]
        controller.run()
        assert mock_print_result.call_count == 2
        assert mock_continue.call_count == 2

    @patch('calculate.view.View.print_menu')
    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    @patch('calculate.view.View.end_message')
    def test_run_with_error_handling(self, mock_end, mock_continue, mock_print_result, 
                                   mock_get_input, mock_print_menu, controller):
        """Test de la gestion des erreurs."""
        mock_get_input.side_effect = ["1", "invalid_operation", "34"]
        controller.run()
        mock_print_result.assert_not_called()
        mock_continue.assert_called_once()

    @patch('calculate.view.View.print_menu')
    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    @patch('calculate.view.View.end_message')
    def test_run_with_empty_input(self, mock_end, mock_continue, mock_print_result, 
                                mock_get_input, mock_print_menu, controller):
        """Test avec une entrée vide."""
        mock_get_input.side_effect = ["", "34"]
        controller.run()
        mock_print_result.assert_not_called()
        mock_continue.assert_not_called()

    @patch('calculate.view.View.print_menu')
    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    @patch('calculate.view.View.end_message')
    def test_run_with_special_characters(self, mock_end, mock_continue, mock_print_result, 
                                       mock_get_input, mock_print_menu, controller):
        """Test avec des caractères spéciaux."""
        mock_get_input.side_effect = ["1", "2 + 3!", "34"]
        controller.run()
        mock_print_result.assert_not_called()
        mock_continue.assert_called_once()

    @patch('calculate.view.View.print_menu')
    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    @patch('calculate.view.View.end_message')
    def test_run_with_help_command(self, mock_end, mock_continue, mock_print_result, 
                                 mock_get_input, mock_print_menu, controller):
        """Test avec la commande d'aide."""
        mock_get_input.side_effect = ["help", "34"]
        controller.run()
        mock_print_result.assert_not_called()
        mock_continue.assert_called_once()

    @patch('calculate.view.View.print_menu')
    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    @patch('calculate.view.View.end_message')
    def test_run_with_statistical_operations(self, mock_end, mock_continue, mock_print_result, 
                                           mock_get_input, mock_print_menu, controller):
        """Test avec des opérations statistiques."""
        mock_get_input.side_effect = ["15", "mean(1,2,3,4,5)", "34"]  # Moyenne
        controller.run()
        mock_print_result.assert_called_once()
        mock_continue.assert_called_once()

    @patch('calculate.view.View.print_menu')
    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    @patch('calculate.view.View.end_message')
    def test_run_with_visualization_operations(self, mock_end, mock_continue, mock_print_result, 
                                             mock_get_input, mock_print_menu, controller):
        """Test avec des opérations de visualisation."""
        mock_get_input.side_effect = ["23", "plot(x^2, -10, 10)", "34"]  # Tracé de fonction
        controller.run()
        mock_print_result.assert_called_once()
        mock_continue.assert_called_once()

    @patch('calculate.view.View.print_menu')
    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    @patch('calculate.view.View.end_message')
    def test_run_with_invalid_operation(self, mock_end, mock_continue, mock_print_result, 
                                      mock_get_input, mock_print_menu, controller):
        """Test avec une opération invalide."""
        mock_get_input.side_effect = ["1", "2 +", "34"]  # Syntaxe invalide
        controller.run()
        mock_print_result.assert_not_called()
        mock_continue.assert_called_once()

    @patch('calculate.view.View.print_menu')
    @patch('calculate.view.View.get_user_input')
    @patch('calculate.view.View.print_result')
    @patch('calculate.view.View.continue_message')
    @patch('calculate.view.View.end_message')
    def test_run_with_complex_operations(self, mock_end, mock_continue, mock_print_result, 
                                       mock_get_input, mock_print_menu, controller):
        """Test avec des opérations complexes."""
        mock_get_input.side_effect = ["21", "correlation(1,2,3;4,5,6)", "34"]  # Corrélation
        controller.run()
        mock_print_result.assert_called_once()
        mock_continue.assert_called_once() 