class IdentityValidator:

    def validate(
        self,
        resume_candidate,
        recruiter_candidate,
    ):

        errors = []

        # -----------------------------
        # Full Name
        # -----------------------------

        if (
            resume_candidate.full_name
            and recruiter_candidate.full_name
        ):

            if (
                resume_candidate.full_name.strip().lower()
                != recruiter_candidate.full_name.strip().lower()
            ):

                errors.append(
                    "Full Name Mismatch\n"
                    f"Resume : {resume_candidate.full_name}\n"
                    f"Recruiter CSV : {recruiter_candidate.full_name}"
                )

        # -----------------------------
        # Email
        # -----------------------------

        if (
            resume_candidate.emails
            and recruiter_candidate.emails
        ):

            if (
                resume_candidate.emails[0].lower()
                != recruiter_candidate.emails[0].lower()
            ):

                errors.append(
                    "Email Mismatch\n"
                    f"Resume : {resume_candidate.emails[0]}\n"
                    f"Recruiter CSV : {recruiter_candidate.emails[0]}"
                )

        # -----------------------------
        # Phone
        # -----------------------------

        if (
            resume_candidate.phones
            and recruiter_candidate.phones
        ):

            resume_phone = (
                resume_candidate.phones[0]
                .replace("+91", "")
                .replace(" ", "")
                .replace("-", "")
            )

            csv_phone = (
                recruiter_candidate.phones[0]
                .replace("+91", "")
                .replace(" ", "")
                .replace("-", "")
            )

            if resume_phone != csv_phone:

                errors.append(
                    "Phone Number Mismatch\n"
                    f"Resume : {resume_candidate.phones[0]}\n"
                    f"Recruiter CSV : {recruiter_candidate.phones[0]}"
                )

        return errors