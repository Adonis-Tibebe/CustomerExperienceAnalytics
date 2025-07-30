# Customer Experience Analytics - Makefile
# Banking App Review Analytics Project

.PHONY: help install install-dev clean test test-cov lint format type-check setup-data scrape-data setup-db load-data run-notebooks docs build dist clean-all

# Default target
help:
	@echo "Customer Experience Analytics - Available Commands:"
	@echo ""
	@echo "📦 Installation:"
	@echo "  install      - Install production dependencies"
	@echo "  install-dev  - Install development dependencies"
	@echo ""
	@echo "🧪 Testing & Quality:"
	@echo "  test         - Run unit tests"
	@echo "  test-cov     - Run tests with coverage report"
	@echo "  lint         - Run flake8 linting"
	@echo "  format       - Format code with black"
	@echo "  type-check   - Run mypy type checking"
	@echo ""
	@echo "🗄️  Data & Database:"
	@echo "  setup-data   - Create necessary data directories"
	@echo "  scrape-data  - Scrape Google Play Store reviews"
	@echo "  setup-db     - Set up Oracle database tables"
	@echo "  load-data    - Load processed data into database"
	@echo ""
	@echo "📊 Analysis:"
	@echo "  run-notebooks - Start Jupyter notebook server"
	@echo ""
	@echo "🧹 Maintenance:"
	@echo "  clean        - Remove Python cache files"
	@echo "  clean-all    - Remove all generated files and caches"
	@echo ""
	@echo "📦 Build:"
	@echo "  build        - Build the package"
	@echo "  dist         - Create distribution files"

# Installation
install:
	@echo "📦 Installing production dependencies..."
	pip install -e .

install-dev:
	@echo "🔧 Installing development dependencies..."
	pip install -e ".[dev,notebooks]"
	@echo "📥 Downloading NLTK data..."
	python -m nltk.downloader punkt stopwords wordnet omw-1.4

# Testing & Quality Assurance
test:
	@echo "🧪 Running unit tests..."
	pytest tests/unit -v

test-cov:
	@echo "🧪 Running tests with coverage..."
	pytest tests/unit --cov=src --cov-report=html --cov-report=term-missing -v

lint:
	@echo "🔍 Running flake8 linting..."
	flake8 src/ tests/ scripts/ --max-line-length=88 --extend-ignore=E203,W503

format:
	@echo "🎨 Formatting code with black..."
	black src/ tests/ scripts/ --line-length=88

type-check:
	@echo "🔍 Running mypy type checking..."
	mypy src/ --ignore-missing-imports

# Data & Database Operations
setup-data:
	@echo "📁 Creating data directories..."
	mkdir -p data/raw/scraped_reviews
	mkdir -p data/processed
	@echo "✅ Data directories created"

scrape-data:
	@echo "🔍 Scraping Google Play Store reviews..."
	python scripts/scrape_playstore.py

setup-db:
	@echo "🗄️ Setting up Oracle database tables..."
	python scripts/oracle_setup.py

load-data:
	@echo "📊 Loading data into Oracle database..."
	python scripts/load_data.py

# Analysis
run-notebooks:
	@echo "📊 Starting Jupyter notebook server..."
	jupyter notebook --notebook-dir=notebooks --ip=0.0.0.0 --port=8888 --no-browser

# Maintenance
clean:
	@echo "🧹 Cleaning Python cache files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	@echo "✅ Cache files cleaned"

clean-all: clean
	@echo "🧹 Cleaning all generated files..."
	rm -rf build/
	rm -rf dist/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	rm -rf .black_cache/
	@echo "✅ All generated files cleaned"

# Build
build:
	@echo "📦 Building package..."
	python -m build

dist: build
	@echo "📦 Creating distribution files..."
	python -m build --sdist --wheel

# Development workflow
dev-setup: install-dev setup-data
	@echo "🚀 Development environment setup complete!"

full-pipeline: scrape-data setup-db load-data
	@echo "🔄 Full data pipeline completed!"

# Quick quality check
quality: format lint type-check test
	@echo "✅ Quality checks completed!"

# CI/CD helpers
ci-test: install-dev test-cov lint type-check
	@echo "✅ CI tests completed!"

# Documentation
docs:
	@echo "📚 Building documentation..."
	# Add documentation building commands here when docs are added
	@echo "📚 Documentation building not yet implemented"

# Environment setup
env-check:
	@echo "🔍 Checking environment..."
	@python -c "import sys; print(f'Python version: {sys.version}')"
	@python -c "import pandas; print(f'Pandas version: {pandas.__version__}')"
	@python -c "import torch; print(f'PyTorch version: {torch.__version__}')"
	@python -c "import transformers; print(f'Transformers version: {transformers.__version__}')"
	@echo "✅ Environment check completed"

# Data validation
validate-data:
	@echo "🔍 Validating data files..."
	@if [ -f "data/processed/cleaned_reviews.csv" ]; then \
		echo "✅ cleaned_reviews.csv found"; \
	else \
		echo "❌ cleaned_reviews.csv not found"; \
	fi
	@if [ -f "data/processed/reviews with sentiments and themes.csv" ]; then \
		echo "✅ reviews with sentiments and themes.csv found"; \
	else \
		echo "❌ reviews with sentiments and themes.csv not found"; \
	fi

# Backup and restore
backup-data:
	@echo "💾 Creating data backup..."
	tar -czf "data_backup_$(date +%Y%m%d_%H%M%S).tar.gz" data/
	@echo "✅ Data backup created"

# Performance testing
benchmark:
	@echo "⚡ Running performance benchmarks..."
	python -m pytest tests/unit -m "slow" -v
	@echo "✅ Benchmark tests completed"

# Security check
security-check:
	@echo "🔒 Running security checks..."
	pip-audit
	@echo "✅ Security check completed"

# Update dependencies
update-deps:
	@echo "🔄 Updating dependencies..."
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt
	@echo "✅ Dependencies updated"
