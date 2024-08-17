FROM public.ecr.aws/lambda/python:3.12

# Copy requirements.txt
# COPY requirements.lock ${LAMBDA_TASK_ROOT}
COPY pyproject.toml ${LAMBDA_TASK_ROOT}
COPY README.md ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir .

# Copy function code
COPY src/javiz ${LAMBDA_TASK_ROOT}/javiz

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "javiz.handler" ]