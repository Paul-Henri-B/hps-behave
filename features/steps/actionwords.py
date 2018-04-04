# encoding: UTF-8
from behave import *
from src.coffee_machine import CoffeeMachine

class Actionwords:
    def __init__(self):
        self.sut = CoffeeMachine()
        self.handled = []

    def i_start_the_coffee_machine_using_language_lang(self, context, lang = "en"):
        self.sut.start(lang)

    def i_shutdown_the_coffee_machine(self, context):
        self.sut.stop()

    def message_message_should_be_displayed(self, context, message = ""):
        assert (self.sut.message == message) is True

    def coffee_should_be_served(self, context):
        assert (self.sut.message == message) is True

    def coffee_should_not_be_served(self, context):
        assert self.sut.coffee_served is False

    def i_take_a_coffee(self, context):
        self.sut.take_coffee()

    def i_empty_the_coffee_grounds(self, context):
        self.sut.empty_grounds()

    def i_fill_the_beans_tank(self, context):
        self.sut.empty_grounds()

    def i_fill_the_water_tank(self, context):
        self.sut.fill_tank()

    def i_take_coffee_number_coffees(self, context, coffee_number = 10):
        coffee_number = int(coffee_number)

        while (coffee_number > 0):
            self.i_take_a_coffee(context)
            coffee_number = coffee_number - 1

            if 'water' in self.handled:
                self.i_fill_the_water_tank(context)

            if 'beans' in self.handled:
                self.i_fill_the_beans_tank(context)

            if 'grounds' in self.handled:
                self.i_empty_the_coffee_grounds(context)

    def the_coffee_machine_is_started(self, context):
        self.i_start_the_coffee_machine_using_language_lang(context)

    def i_handle_everything_except_the_water_tank(self, context):
        self.i_handle_coffee_grounds(context)
        self.i_handle_beans(context)

    def i_handle_water_tank(self, context):
        self.handled.append('water')

    def i_handle_beans(self, context):
        self.handled.append('beans')

    def i_handle_coffee_grounds(self, context):
        self.handled.append('grounds')

    def i_handle_everything_except_the_beans(self, context):
        self.i_handle_water_tank(context)
        self.i_handle_coffee_grounds(context)

    def i_handle_everything_except_the_grounds(self, context):
        self.i_handle_water_tank(context)
        self.i_handle_beans(context)

    def displayed_message_is(self, context, free_text = ""):
        self.message_message_should_be_displayed(context, message = __free_text)

    def i_switch_to_settings_mode(self, context):
        self.sut.show_settings()

    def settings_should_be(self, context, datatable = "||"):
        # Apparently, no way to get the raw table and assert_equals does not work that much ...
        expected = [datatable.rows[0].headings]
        for row in datatable.rows:
            expected.append([c for c in row])

        assert (expected == [[str(k), str(v)] for k, v in self.sut.get_settings().items()]) is True
