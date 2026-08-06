CREATE TABLE IF NOT EXISTS users (

    id BIGSERIAL PRIMARY KEY,

    email VARCHAR(255) UNIQUE NOT NULL,

    password_hash TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS profiles (

    id BIGSERIAL PRIMARY KEY,

    user_id BIGINT REFERENCES users(id),

    first_name VARCHAR(100),

    last_name VARCHAR(100),

    location VARCHAR(200),

    target_role VARCHAR(200),

    years_experience INTEGER,

    summary TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS preferences (

    id BIGSERIAL PRIMARY KEY,

    user_id BIGINT REFERENCES users(id),

    preferred_location VARCHAR(200),

    remote_preference VARCHAR(50),

    target_salary INTEGER,

    job_type VARCHAR(50),

    sponsorship_required BOOLEAN,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS skills (

    id BIGSERIAL PRIMARY KEY,

    profile_id BIGINT REFERENCES profiles(id),

    skill_name VARCHAR(100),

    skill_level VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS resumes (

    id BIGSERIAL PRIMARY KEY,

    profile_id BIGINT REFERENCES profiles(id),

    file_name VARCHAR(255),

    storage_path TEXT,

    extracted_text TEXT,

    version INTEGER DEFAULT 1,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS contacts (

    id BIGSERIAL PRIMARY KEY,

    user_id BIGINT REFERENCES users(id),

    name VARCHAR(200),

    company VARCHAR(200),

    role VARCHAR(200),

    email VARCHAR(255),

    linkedin_url TEXT,

    relationship_type VARCHAR(100),

    notes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS job_postings (

    id BIGSERIAL PRIMARY KEY,

    external_job_id VARCHAR(200),

    title VARCHAR(300),

    company VARCHAR(200),

    location VARCHAR(200),

    description TEXT,

    url TEXT,

    source VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS saved_jobs (

    id BIGSERIAL PRIMARY KEY,

    user_id BIGINT REFERENCES users(id),

    job_id BIGINT REFERENCES job_postings(id),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS applications (

    id BIGSERIAL PRIMARY KEY,

    user_id BIGINT REFERENCES users(id),

    job_id BIGINT REFERENCES job_postings(id),

    status VARCHAR(50),

    applied_date DATE,

    notes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS interview_notes (

    id BIGSERIAL PRIMARY KEY,

    application_id BIGINT REFERENCES applications(id),

    question TEXT,

    answer TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- Job postings fetched from external APIs
CREATE TABLE IF NOT EXISTS job_postings (
    id SERIAL PRIMARY KEY,

    external_id VARCHAR(255) UNIQUE NOT NULL,

    title VARCHAR(255) NOT NULL,
    company VARCHAR(255),

    location VARCHAR(255),

    description TEXT,

    url TEXT,

    source VARCHAR(50) DEFAULT 'RemoteOK',

    skills TEXT,

    match_score INTEGER,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User saved jobs
CREATE TABLE IF NOT EXISTS saved_jobs (
    id SERIAL PRIMARY KEY,

    user_id INTEGER NOT NULL,

    job_id INTEGER NOT NULL,

    status VARCHAR(50) DEFAULT 'saved',

    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_saved_job
        FOREIGN KEY(job_id)
        REFERENCES job_postings(id)
        ON DELETE CASCADE
);

-- =========================
-- INDEXES
-- =========================

CREATE INDEX IF NOT EXISTS idx_profiles_user_id
ON profiles(user_id);


CREATE INDEX IF NOT EXISTS idx_applications_user_id
ON applications(user_id);


CREATE INDEX IF NOT EXISTS idx_saved_jobs_user_id
ON saved_jobs(user_id);


CREATE INDEX IF NOT EXISTS idx_saved_jobs_job_id
ON saved_jobs(job_id);


CREATE INDEX IF NOT EXISTS idx_applications_job_id
ON applications(job_id);

-- Future CDF Tables

-- Later we can create:

-- Delta Lake

-- analytics/

-- ├── profile_changes

-- ├── resume_upload_events

-- ├── job_activity

-- ├── application_events

-- └── user_activity

