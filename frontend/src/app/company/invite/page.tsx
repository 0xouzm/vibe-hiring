"use client";

import { useState } from "react";
import { api } from "@/lib/api";
import { useAuth } from "@/hooks/useAuth";
import { Card, CardHeader, CardContent } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";

/* -- Types ------------------------------------------------------------ */

interface InviteResult {
  user_id: string;
  email: string;
  message: string;
}

/* -- Invite Team Members Page ----------------------------------------- */

export default function InvitePage() {
  const { user } = useAuth();
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [invites, setInvites] = useState<InviteResult[]>([]);

  const companyId = user?.company_id;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!companyId || !email.trim() || !name.trim()) return;

    setSubmitting(true);
    setError(null);

    try {
      const result = await api.post<InviteResult>(
        `/companies/${companyId}/invite`,
        { email: email.trim(), name: name.trim() },
      );
      setInvites((prev) => [result, ...prev]);
      setEmail("");
      setName("");
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "Failed to send invitation.",
      );
    } finally {
      setSubmitting(false);
    }
  };

  if (!companyId) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <p className="text-text-dim text-sm">
          No company associated with your account.
        </p>
      </div>
    );
  }

  return (
    <div className="max-w-xl mx-auto">
      <div className="mb-8">
        <h1 className="text-2xl font-bold font-display text-text">
          Invite Team Members
        </h1>
        <p className="text-sm text-text-dim mt-1">
          Invite team members to complete the Company DNA survey for a more
          accurate culture profile.
        </p>
      </div>

      {/* Invite form */}
      <Card>
        <CardHeader>
          <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
            Send Invitation
          </h2>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="flex flex-col gap-4">
            <div>
              <label
                htmlFor="invite-name"
                className="block text-sm font-medium text-text mb-1"
              >
                Full Name
              </label>
              <input
                id="invite-name"
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Jane Smith"
                required
                className="w-full px-3 py-2 rounded-[var(--radius)] bg-surface-light border border-glass-border text-text text-sm placeholder:text-text-muted focus:outline-none focus:ring-2 focus:ring-indigo/40"
              />
            </div>

            <div>
              <label
                htmlFor="invite-email"
                className="block text-sm font-medium text-text mb-1"
              >
                Email Address
              </label>
              <input
                id="invite-email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="jane@company.com"
                required
                className="w-full px-3 py-2 rounded-[var(--radius)] bg-surface-light border border-glass-border text-text text-sm placeholder:text-text-muted focus:outline-none focus:ring-2 focus:ring-indigo/40"
              />
            </div>

            {error && <p className="text-rose text-sm">{error}</p>}

            <Button type="submit" loading={submitting} disabled={submitting}>
              Send Invitation
            </Button>
          </form>
        </CardContent>
      </Card>

      {/* Success list */}
      {invites.length > 0 && (
        <Card className="mt-6">
          <CardHeader>
            <h2 className="text-sm font-semibold text-text-dim uppercase tracking-wide">
              Sent Invitations
            </h2>
          </CardHeader>
          <CardContent>
            <ul className="divide-y divide-glass-border">
              {invites.map((inv) => (
                <li
                  key={inv.user_id}
                  className="py-3 flex items-center justify-between"
                >
                  <div>
                    <p className="text-sm font-medium text-text">
                      {inv.email}
                    </p>
                    <p className="text-xs text-text-muted">{inv.message}</p>
                  </div>
                  <div className="w-2 h-2 rounded-full bg-emerald shrink-0" />
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
