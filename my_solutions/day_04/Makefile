RED	= \033[0;31m
NC	= \033[0m

all:
	@python3 main.py "input.txt"

test1:
	@echo "\n$(RED)--- Running tests ---$(NC)"
	@python3 main.py "input_test_p1.txt"

test2:
	@echo "\n$(RED)--- Running tests - all invalid ---$(NC)"
	@python3 main.py "input_test_p2_invalid.txt"
	@echo "\n$(RED)--- Running tests - all valid ---$(NC)"
	@python3 main.py "input_test_p2_valid.txt"
