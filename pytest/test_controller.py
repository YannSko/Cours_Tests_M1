import pytest
from unittest.mock import patch, MagicMock
from calculate.controller import Controller
from calculate.view import View
from calculate.operators import Operators

@pytest.fixture
def controller_mocks():
    """Fixture pour créer un contrôleur avec des mocks."""
    mock_view = MagicMock(spec=View)
    mock_operators = MagicMock(spec=Operators)
    controller = Controller(mock_view, mock_operators)
    return controller, mock_view, mock_operators

class TestController:
    """Tests unitaires pour le Controller."""
    
    def test_init(self, controller_mocks):
        """Test l'initialisation du Controller."""
        controller, mock_view, mock_operators = controller_mocks
        assert controller.view == mock_view
        assert controller.operators == mock_operators
    
    def test_init_error(self):
        """Test la gestion d'erreur pendant l'initialisation."""
        mock_view = MagicMock(spec=View)
        mock_operators = MagicMock(spec=Operators)
        
        with pytest.raises(ValueError):
            Controller(None, mock_operators)
            
        with pytest.raises(ValueError):
            Controller(mock_view, None)
    
    def test_is_input_valid(self, controller_mocks):
        """Test la validation de l'entrée utilisateur."""
        controller, _, _ = controller_mocks
        
        # Entrées valides
        assert controller._is_input_valid("2 + 3") is True
        assert controller._is_input_valid("sqrt(16)") is True
        assert controller._is_input_valid("mean(1,2,3,4,5)") is True
        assert controller._is_input_valid("help") is True
        assert controller._is_input_valid("exit") is True
        
        # Entrées invalides
        assert controller._is_input_valid("") is False
        assert controller._is_input_valid("   ") is False
        assert controller._is_input_valid("invalid command") is False
    
    def test_is_quit(self, controller_mocks):
        """Test la condition de sortie."""
        controller, _, _ = controller_mocks
        
        # Commandes de sortie
        assert controller._is_quit("exit") is True
        assert controller._is_quit("quit") is True
        assert controller._is_quit("q") is True
        
        # Commandes qui ne sont pas des sorties
        assert controller._is_quit("help") is False
        assert controller._is_quit("2 + 3") is False
        assert controller._is_quit("") is False
        assert controller._is_quit(None) is False
    
    def test_operations_basic(self, controller_mocks):
        """Test les opérations mathématiques de base."""
        controller, _, mock_operators = controller_mocks
        
        # Configuration des mocks
        mock_operators.addition.return_value = 5
        mock_operators.substraction.return_value = 2
        mock_operators.multiplication.return_value = 6
        mock_operators.division.return_value = 3
        
        # Addition
        result = controller._operations("2 + 3")
        assert result == 5
        mock_operators.addition.assert_called_once_with(2, 3)
        
        # Soustraction
        result = controller._operations("5 - 3")
        assert result == 2
        mock_operators.substraction.assert_called_once_with(5, 3)
        
        # Multiplication
        result = controller._operations("2 * 3")
        assert result == 6
        mock_operators.multiplication.assert_called_once_with(2, 3)
        
        # Division
        result = controller._operations("6 / 2")
        assert result == 3
        mock_operators.division.assert_called_once_with(6, 2)
    
    def test_operations_advanced(self, controller_mocks):
        """Test les opérations mathématiques avancées."""
        controller, _, mock_operators = controller_mocks
        
        # Configuration des mocks
        mock_operators.square_root.return_value = 4
        mock_operators.power.return_value = 8
        mock_operators.logarithm.return_value = 0
        mock_operators.modulo.return_value = 1
        mock_operators.sine.return_value = 0
        mock_operators.cosine.return_value = 1
        mock_operators.tangent.return_value = 0
        mock_operators.factorial.return_value = 120
        mock_operators.absolute.return_value = 5
        mock_operators.exponential.return_value = 1
        
        # Racine carrée
        result = controller._operations("sqrt(16)")
        assert result == 4
        mock_operators.square_root.assert_called_once_with(16)
        
        # Puissance
        result = controller._operations("2 ^ 3")
        assert result == 8
        mock_operators.power.assert_called_once_with(2, 3)
        
        # Logarithme
        result = controller._operations("log(1)")
        assert result == 0
        mock_operators.logarithm.assert_called_once_with(1)
        
        # Modulo
        result = controller._operations("5 % 2")
        assert result == 1
        mock_operators.modulo.assert_called_once_with(5, 2)
        
        # Sinus
        result = controller._operations("sin(0)")
        assert result == 0
        mock_operators.sine.assert_called_once_with(0)
        
        # Cosinus
        result = controller._operations("cos(0)")
        assert result == 1
        mock_operators.cosine.assert_called_once_with(0)
        
        # Tangente
        result = controller._operations("tan(0)")
        assert result == 0
        mock_operators.tangent.assert_called_once_with(0)
        
        # Factorielle
        result = controller._operations("5!")
        assert result == 120
        mock_operators.factorial.assert_called_once_with(5)
        
        # Valeur absolue
        result = controller._operations("abs(-5)")
        assert result == 5
        mock_operators.absolute.assert_called_once_with(-5)
        
        # Exponentielle
        result = controller._operations("exp(0)")
        assert result == 1
        mock_operators.exponential.assert_called_once_with(0)
    
    def test_operations_statistics(self, controller_mocks):
        """Test les opérations statistiques."""
        controller, _, mock_operators = controller_mocks
        
        # Configuration des mocks
        mock_operators.mean.return_value = 3
        mock_operators.median.return_value = 3
        mock_operators.mode.return_value = 3
        mock_operators.standard_deviation.return_value = 1.414
        mock_operators.variance.return_value = 2
        mock_operators.percentile.return_value = 3
        mock_operators.correlation.return_value = 1
        mock_operators.linear_regression.return_value = (1, 3)
        
        # Moyenne
        result = controller._operations("mean(1,2,3,4,5)")
        assert result == 3
        mock_operators.mean.assert_called_once_with([1, 2, 3, 4, 5])
        
        # Médiane
        result = controller._operations("median(1,2,3,4,5)")
        assert result == 3
        mock_operators.median.assert_called_once_with([1, 2, 3, 4, 5])
        
        # Mode
        result = controller._operations("mode(1,2,3,3,3)")
        assert result == 3
        mock_operators.mode.assert_called_once_with([1, 2, 3, 3, 3])
        
        # Écart-type
        result = controller._operations("std(1,2,3,4,5)")
        assert result == 1.414
        mock_operators.standard_deviation.assert_called_once_with([1, 2, 3, 4, 5])
        
        # Variance
        result = controller._operations("var(1,2,3,4,5)")
        assert result == 2
        mock_operators.variance.assert_called_once_with([1, 2, 3, 4, 5])
        
        # Percentile
        result = controller._operations("percentile(1,2,3,4,5;50)")
        assert result == 3
        mock_operators.percentile.assert_called_once_with([1, 2, 3, 4, 5], 50)
        
        # Corrélation
        result = controller._operations("correlation(1,2,3;4,5,6)")
        assert result == 1
        mock_operators.correlation.assert_called_once_with([1, 2, 3], [4, 5, 6])
        
        # Régression linéaire
        result = controller._operations("regression(1,2,3;4,5,6)")
        assert result == (1, 3)
        mock_operators.linear_regression.assert_called_once_with([1, 2, 3], [4, 5, 6])
    
    def test_operations_visualization(self, controller_mocks):
        """Test les opérations de visualisation."""
        controller, _, mock_operators = controller_mocks
        
        # Configuration des mocks
        mock_operators.plot.return_value = True
        mock_operators.scatter.return_value = True
        mock_operators.histogram.return_value = True
        mock_operators.polar.return_value = True
        mock_operators.plot_3d.return_value = True
        mock_operators.boxplot.return_value = True
        mock_operators.qq_plot.return_value = True
        mock_operators.heatmap.return_value = True
        mock_operators.pie_chart.return_value = True
        mock_operators.bar_chart.return_value = True
        
        # Plot
        result = controller._operations("plot(x**2,-10,10,graph.png)")
        assert result is True
        mock_operators.plot.assert_called_once_with("x**2", -10, 10, "graph.png")
        
        # Scatter
        result = controller._operations("scatter(1,2,3;4,5,6;scatter.png)")
        assert result is True
        mock_operators.scatter.assert_called_once_with([1, 2, 3], [4, 5, 6], "scatter.png")
        
        # Histogram
        result = controller._operations("histogram(1,2,2,3,3,3;hist.png)")
        assert result is True
        mock_operators.histogram.assert_called_once_with([1, 2, 2, 3, 3, 3], "hist.png")
        
        # Polar
        result = controller._operations("polar(0,1.57,3.14;1,2,3;polar.png)")
        assert result is True
        mock_operators.polar.assert_called_once_with([0, 1.57, 3.14], [1, 2, 3], "polar.png")
        
        # 3D
        result = controller._operations("3d(1,2;3,4;5,6;3d.png)")
        assert result is True
        mock_operators.plot_3d.assert_called_once_with([1, 2], [3, 4], [5, 6], "3d.png")
        
        # Boxplot
        result = controller._operations("boxplot(1,2,3,4,5;boxplot.png)")
        assert result is True
        mock_operators.boxplot.assert_called_once_with([1, 2, 3, 4, 5], "boxplot.png")
        
        # QQ plot
        result = controller._operations("qq(1,2,3,4,5;qq.png)")
        assert result is True
        mock_operators.qq_plot.assert_called_once_with([1, 2, 3, 4, 5], "qq.png")
        
        # Heatmap
        result = controller._operations("heatmap(1,2;3,4;heatmap.png)")
        assert result is True
        mock_operators.heatmap.assert_called_once_with([[1, 2], [3, 4]], "heatmap.png")
        
        # Pie chart
        result = controller._operations("pie(1,2,3;A,B,C;pie.png)")
        assert result is True
        mock_operators.pie_chart.assert_called_once_with([1, 2, 3], ["A", "B", "C"], "pie.png")
        
        # Bar chart
        result = controller._operations("bar(1,2,3;A,B,C;bar.png)")
        assert result is True
        mock_operators.bar_chart.assert_called_once_with([1, 2, 3], ["A", "B", "C"], "bar.png")
    
    def test_operations_error_handling(self, controller_mocks):
        """Test la gestion des erreurs dans les opérations."""
        controller, mock_view, mock_operators = controller_mocks
        
        # Division par zéro
        mock_operators.division.side_effect = ValueError("Division par zéro")
        result = controller._operations("5 / 0")
        assert result is None
        mock_view.print_error.assert_called_once_with("Division par zéro")
        
        # Réinitialisation du mock
        mock_view.print_error.reset_mock()
        
        # Opération invalide
        result = controller._operations("invalid operation")
        assert result is None
        mock_view.print_error.assert_called_once_with("Opération non prise en charge: invalid operation")
    
    def test_run_basic_cycle(self, controller_mocks):
        """Test le cycle d'exécution de base."""
        controller, mock_view, mock_operators = controller_mocks
        
        # Configuration des mocks
        mock_view.get_user_input.side_effect = ["2 + 3", "exit"]
        mock_operators.addition.return_value = 5
        
        # Exécution
        controller.run()
        
        # Vérifications
        mock_view.print_welcome.assert_called_once()
        mock_view.print_menu.assert_called()
        mock_view.get_user_input.assert_called()
        mock_operators.addition.assert_called_once_with(2, 3)
        mock_view.print_result.assert_called_once_with("2 + 3", 5)
        mock_view.continue_message.assert_called_once()
        mock_view.end_message.assert_called_once()
    
    def test_run_with_help_commands(self, controller_mocks):
        """Test l'exécution avec les commandes d'aide."""
        controller, mock_view, _ = controller_mocks
        
        # Configuration des mocks
        mock_view.get_user_input.side_effect = ["help", "help stats", "help visualization", "exit"]
        
        # Exécution
        controller.run()
        
        # Vérifications
        mock_view.print_welcome.assert_called_once()
        mock_view.print_help.assert_called_once()
        mock_view.print_statistics_help.assert_called_once()
        mock_view.print_visualization_help.assert_called_once()
        mock_view.end_message.assert_called_once()
    
    def test_run_with_error(self, controller_mocks):
        """Test l'exécution avec une erreur."""
        controller, mock_view, _ = controller_mocks
        
        # Configuration des mocks
        mock_view.get_user_input.side_effect = Exception("Erreur simulée")
        
        # Exécution
        controller.run()
        
        # Vérifications
        mock_view.print_welcome.assert_called_once()
        mock_view.print_error.assert_called_with("Erreur lors de l'exécution: Erreur simulée")
        mock_view.end_message.assert_called_once()
    
    def test_run_with_invalid_input(self, controller_mocks):
        """Test l'exécution avec une entrée invalide."""
        controller, mock_view, _ = controller_mocks
        
        # Configuration des mocks
        mock_view.get_user_input.side_effect = ["invalid command", "exit"]
        
        # Exécution
        controller.run()
        
        # Vérifications
        mock_view.print_welcome.assert_called_once()
        mock_view.print_error.assert_called_with("Entrée invalide")
        mock_view.end_message.assert_called_once()
    
    def test_run_with_empty_input(self, controller_mocks):
        """Test l'exécution avec une entrée vide."""
        controller, mock_view, _ = controller_mocks
        
        # Configuration des mocks
        mock_view.get_user_input.side_effect = ["", "exit"]
        
        # Exécution
        controller.run()
        
        # Vérifications
        mock_view.print_welcome.assert_called_once()
        mock_view.print_error.assert_called_with("Entrée invalide")
        mock_view.end_message.assert_called_once()
    
    def test_run_with_multiple_operations(self, controller_mocks):
        """Test l'exécution avec plusieurs opérations."""
        controller, mock_view, mock_operators = controller_mocks
        
        # Configuration des mocks
        mock_view.get_user_input.side_effect = ["2 + 3", "5 - 2", "exit"]
        mock_operators.addition.return_value = 5
        mock_operators.substraction.return_value = 3
        
        # Exécution
        controller.run()
        
        # Vérifications
        assert mock_view.print_result.call_count == 2
        mock_operators.addition.assert_called_once_with(2, 3)
        mock_operators.substraction.assert_called_once_with(5, 2)
        mock_view.continue_message.assert_called()
        mock_view.end_message.assert_called_once()
    
    def test_handle_help_command(self, controller_mocks):
        """Test la gestion des commandes d'aide."""
        controller, mock_view, _ = controller_mocks
        
        # Aide générale
        controller._handle_help_command("help")
        mock_view.print_help.assert_called_once()
        
        # Aide statistique
        controller._handle_help_command("help stats")
        mock_view.print_statistics_help.assert_called_once()
        
        # Aide visualisation
        controller._handle_help_command("help visualization")
        mock_view.print_visualization_help.assert_called_once()
        
        # Aide inconnue
        controller._handle_help_command("help unknown")
        mock_view.print_error.assert_called_once_with("Commande d'aide non reconnue: unknown")
    
    def test_is_help_command(self, controller_mocks):
        """Test la détection des commandes d'aide."""
        controller, _, _ = controller_mocks
        
        # Commandes d'aide
        assert controller._is_help_command("help") is True
        assert controller._is_help_command("help stats") is True
        assert controller._is_help_command("help visualization") is True
        
        # Commandes qui ne sont pas de l'aide
        assert controller._is_help_command("exit") is False
        assert controller._is_help_command("2 + 3") is False
        assert controller._is_help_command("") is False 