'use client';
import { supabase } from '@/lib/supabase';
import { useEffect, useState } from 'react';

export default function TestDbPage() {
  const [dbStatus, setDbStatus] = useState<string>('Testing...');
  const [backendStatus, setBackendStatus] = useState<string>('Testing...');

  useEffect(() => {
    async function checkSupabase() {
      try {
        const { error } = await supabase.from('non_existent_table').select('*').limit(1);
        // Simplest check: Auth.
        const { data: { session }, error: authError } = await supabase.auth.getSession();
        if (authError) throw authError;
        setDbStatus('Connected to Supabase (Client accessible)');
      } catch (e: any) {
        setDbStatus(`Connection Error: ${e.message}`);
      }
    }

    async function checkBackend() {
      try {
        const res = await fetch('http://localhost:8000/health/db');
        const data = await res.json();
        if (data.status === 'ok') {
            setBackendStatus('Connected to Backend DB');
        } else {
            setBackendStatus(`Backend Error: ${data.detail || 'Unknown'}`);
        }
      } catch (e: any) {
        setBackendStatus(`Fetch Error: ${e.message}`);
      }
    }

    checkSupabase();
    checkBackend();
  }, []);

  return (
    <div className="p-10 font-sans text-white/90 bg-gray-900 min-h-screen">
        <h1 className="text-2xl font-bold mb-6 text-emerald-400">System Status Check</h1>
        
        <div className="space-y-4">
            <div className="p-4 border border-white/10 rounded bg-white/5">
                <h2 className="font-semibold text-lg text-white">Frontend (Supabase Client)</h2>
                <p className="mt-2">{dbStatus}</p>
            </div>

            <div className="p-4 border border-white/10 rounded bg-white/5">
                <h2 className="font-semibold text-lg text-white">Backend (SQLAlchemy)</h2>
                <p className="mt-2">{backendStatus}</p>
            </div>
        </div>
    </div>
  );
}
