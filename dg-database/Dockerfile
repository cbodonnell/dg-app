# Use the official PostgreSQL image as the base image
FROM postgres

# Default environment variables for the PostgreSQL
ENV POSTGRES_USERNAME=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=dg_database

# Expose the PostgreSQL port
EXPOSE 5432

# Set the data directory for PostgreSQL
VOLUME /var/lib/postgresql/data

# The default command to run when the container starts
CMD ["postgres"]