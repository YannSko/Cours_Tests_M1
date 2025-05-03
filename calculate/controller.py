from calculate.view import View
from calculate.operators import Operators

class Controller:
    def __init__(self):
        self.operator = Operators()
        self.result = None

    def run(self):
        """
        Run the principal Menu and the user can choice
        which operation he would like to use.
        """
        View.print_menu()
        is_home_menu_run = True
        while is_home_menu_run:
            input_msg = "Entrez votre choix"
            user_input = View.get_user_input(input_msg)
            if self._is_input_valid(user_input):
                if user_input == "help":
                    View.print_visualization_help()
                else:
                    self._operations(user_input)
                View.print_menu()
            is_home_menu_run = self._is_quit(user_input)
        View.end_message()

    def _is_input_valid(self, user_input):
        """
        Checks if the input corresponds to a possibility of operations.

        :param user_input: User input enter in the method run().
        :return: Return True if the input corresponds to a possibility of operations
                 otherwise it return False.
        """
        return user_input in [str(i) for i in range(1, 35)] or user_input == "help"

    def _operations(self, user_input):
        """
        Calls the function corresponding with the operation ask by the user and
        get the user operation by an input.

        :param user_input: User input enter in the method run().
        """
        input_msg = "Entrez votre opération"
        operation = View.get_user_input(input_msg)

        try:
            # Opérations de base
            if user_input == "1":
                self.result = self.operator.addition(operation)
            elif user_input == "2":
                self.result = self.operator.substraction(operation)
            elif user_input == "3":
                self.result = self.operator.multiplication(operation)
            elif user_input == "4":
                self.result = self.operator.division(operation)
            elif user_input == "5":
                self.result = self.operator.power(operation)
            elif user_input == "6":
                self.result = self.operator.square_root(operation)
            elif user_input == "7":
                self.result = self.operator.logarithm(operation)
            elif user_input == "8":
                self.result = self.operator.modulo(operation)
            elif user_input == "9":
                self.result = self.operator.sine(operation)
            elif user_input == "10":
                self.result = self.operator.cosine(operation)
            elif user_input == "11":
                self.result = self.operator.tangent(operation)
            elif user_input == "12":
                self.result = self.operator.factorial(operation)
            elif user_input == "13":
                self.result = self.operator.absolute(operation)
            elif user_input == "14":
                self.result = self.operator.exponential(operation)
            
            # Statistiques
            elif user_input == "15":
                self.result = self.operator.mean(operation)
            elif user_input == "16":
                self.result = self.operator.median(operation)
            elif user_input == "17":
                self.result = self.operator.mode(operation)
            elif user_input == "18":
                self.result = self.operator.standard_deviation(operation)
            elif user_input == "19":
                self.result = self.operator.variance(operation)
            elif user_input == "20":
                self.result = self.operator.percentile(operation)
            elif user_input == "21":
                self.result = self.operator.correlation(operation)
            elif user_input == "22":
                self.result = self.operator.linear_regression(operation)
            
            # Visualisation
            elif user_input in [str(i) for i in range(23, 33)]:
                self.result = self.operator.visualize(operation)

            View.print_result(operation, self.result)
        except ValueError as e:
            print(f"\nErreur: {str(e)}")
        except Exception as e:
            print(f"\nUne erreur inattendue s'est produite: {str(e)}")
        
        View.continue_message()

    def _is_quit(self, user_input):
        """
        Checks if the user ask for stop the script thanks to the input enter
        in the method run().

        :param user_input: User input enter in the method run().
        :return: True if the user ask for exit the script.
        """
        return not user_input == "34" 