import click
from typing import Tuple


@click.group()
def interpretable_models_cli():
    """
    Illustrates the concepts of interpretable models.
    """
    pass


@click.command()
@click.option(
    "--task",
    type=click.Choice(["regr", "class"], case_sensitive=False),
    required=True,
    help="Task type: regression (regr) or classification (class).",
)
def select_model(task: str) -> Tuple[str, bool, bool, bool]:
    """
    Selects a suitable interpretable model based on the task type.
    """
    models = [
        {
            "algorithm": "Linear regression",
            "linear": True,
            "monotone": True,
            "interaction": False,
            "task": "regr",
        },
        {
            "algorithm": "Logistic regression",
            "linear": False,
            "monotone": True,
            "interaction": False,
            "task": "class",
        },
        {
            "algorithm": "Decision trees",
            "linear": False,
            "monotone": False,
            "interaction": True,
            "task": "class,regr",
        },
        {
            "algorithm": "RuleFit",
            "linear": True,
            "monotone": False,
            "interaction": True,
            "task": "class,regr",
        },
        {
            "algorithm": "Naive Bayes",
            "linear": False,
            "monotone": True,
            "interaction": False,
            "task": "class",
        },
        {
            "algorithm": "K-nearest neighbors",
            "linear": False,
            "monotone": False,
            "interaction": False,
            "task": "class,regr",
        },
    ]

    selected_models = [model for model in models if task in model["task"]]

    click.echo(f"Interpretable models suitable for {task} task:")

    for model in selected_models:
        click.echo(f"  - {model['algorithm']}")

    return selected_models


interpretable_models_cli.add_command(select_model)


if __name__ == "__main__":
    interpretable_models_cli()
