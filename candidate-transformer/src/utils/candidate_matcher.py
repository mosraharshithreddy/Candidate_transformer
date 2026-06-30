class CandidateMatcher:

    def find_match(self, recruiter_rows, resume_candidate):

        # -----------------------------
        # 1. Match by Email
        # -----------------------------
        if resume_candidate.emails:

            resume_email = resume_candidate.emails[0].strip().lower()

            for row in recruiter_rows:

                csv_email = row.get("email", "").strip().lower()

                if csv_email == resume_email:
                    return row

        # -----------------------------
        # 2. Match by Phone
        # -----------------------------
        if resume_candidate.phones:

            resume_phone = (
                resume_candidate.phones[0]
                .replace("+91", "")
                .replace(" ", "")
                .replace("-", "")
            )

            for row in recruiter_rows:

                csv_phone = (
                    row.get("phone", "")
                    .replace("+91", "")
                    .replace(" ", "")
                    .replace("-", "")
                )

                if csv_phone == resume_phone:
                    return row

        # -----------------------------
        # 3. Match by Full Name
        # -----------------------------
        if resume_candidate.full_name:

            resume_name = (
                resume_candidate.full_name
                .strip()
                .lower()
            )

            for row in recruiter_rows:

                csv_name = (
                    row.get("full_name", "")
                    .strip()
                    .lower()
                )

                if csv_name == resume_name:
                    return row

        return None